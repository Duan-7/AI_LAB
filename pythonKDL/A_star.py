import queue
import draw 
#Hàm chuyển trạng thái dạng ma trận sang chuỗi để dễ xử lý
def convert_str(data: str) -> str:
    len_data = len(data)
    result = ""
    for i in range(len_data):
        for j in range(len_data):
            result += str(data[i][j])
    return result
# Chuyển trạng thái (kiểu chuỗi) sang lại ma trận 3x3 dùng để xuất đáp án
def convert_list(data: str)-> list[list[int]]:
    string_dt,index = data,0
    len_list = int(len(string_dt)**(1/2))
    result = [[0]*len_list for _ in range(len_list)]
    for i in range(len_list):
        for j in range(len_list):
            result[i][j] = int(string_dt[index])
            index += 1
    return result

def find_index(s: str)-> tuple[int,int]:
    local = s.find('9',0)
    return  (local//3,local - (local//3)*3)

# Chuyển trạng thái string_dt sang trạng thái mới có id trong matrix lalf new_index
def swap_status(string_dt: str,new_index: tuple[int,int]) -> str:
    vt_o = find_index(string_dt)
    local_old = vt_o[0]*3 + vt_o[1]
    local_new = new_index[0]*3 + new_index[1]
    # Vì swap 2 trạng thái như nhau nên ta mặc định chuyển về local_new > local_old
    if local_new < local_old:
        tmp = local_old
        local_old = local_new
        local_new = tmp
    # Thực hiện đổi trạng thái trực tiếp trên chuỗi bằng thao tác cắt ghép xử lýchuỗi 
    string_new = string_dt[:local_old] + string_dt[local_new] + string_dt[local_old+1:local_new] + string_dt[local_old] + string_dt[local_new+1:]
    return string_new

# Phép cộng hai tuple
def sum_(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0],a[1]+b[1])
# Tính giá trị h(n): là số vị trí sai của cur_status so với goal
def hn(s1: str, s2 : str) -> int:
    return int(sum([s1[i]!=s2[i] for i in range(len(s1))]))

# Truy vết đường đi
def Path(s: str,t: str,trace: dict) -> list[str]:
    trace_path = []
    if t not in trace: return []
    while 1:
        trace_path.append(t)
        if t == s: break
        t = trace[t]
    trace_path.reverse()
    return trace_path
# Thuật toán A* với:
# h(n) là hàm đánh giá độ tương thích với đáp án gần nhất (có bao nhiêu vị trí bị lệch với đáp án)
# g(n) là độ sâu của node
def A_star(start: str,goal: str) -> list[str]:
    # khởi tạo priority_queue với kiểu tuple(f(n),n_status): độ ưu tiên f(n), n_status: trạng thái n kiếu str
    q = queue.PriorityQueue()
    fn,g_n,trace = dict(),dict(),dict()
    q.put((0,start))
    status = [(0,-1),(0,1),(1,0),(-1,0)]
    visited = set()
    visited.add(start)
    g_n[start] = 0
    while(not q.empty()):
        _,current_status = q.get()
        if current_status == goal:
            break
        index = find_index(current_status)
        for tus in status:
            x,y = sum_(tus,index)
            if x>=0 and x < 3 and y >= 0 and y < 3:
                new_status = swap_status(current_status,(x,y))
                if new_status not in visited:
                    h_n = hn(new_status,goal)
                    g_n[new_status] = g_n[current_status] + 1
                    fn[new_status] = g_n[new_status] + h_n
                    q.put((fn[new_status],new_status))
                    trace[new_status] = current_status
                    visited.add(new_status)
    return Path(start, goal , trace)

if __name__=='__main__':
    #Dữ liệu vào là ma trận số nguyên và quy ước vị trí ô trống là số 9
    start_status = [[7,2,4],[5,9,6],[8,3,1]]
    goal_status = [[9,1,2],[3,4,5],[6,7,8]]
    s = convert_str(start_status)
    t = convert_str(goal_status)
    result = A_star(s,t)
    #in ra các bước thực hiện giải bài toán
    print("So buoc giai la:",len(result) - 1) 
    for i in range(len(result)):
        print("Buoc:",i)
        kq = convert_list(result[i])
        for u in range(len(kq)):
            for v in range(len(kq)):
                print(kq[u][v],end=" ")
            print()