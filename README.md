# AI-Project1-Search

# depthFirstSearch
  - Lấy ra trạng thái ban đầu của agent và kiểm tra goal state
  - Tạo list visited lưu các state đã đi qua
  - Tạo stack lưu state 
  - Push trạng thái ban đầu và đường đi đến trạng thái đó, hiện tại là rỗng
  - Tao vòng lặp khi stack còn phần tử thì duyệt
      + Lấy ra State CUỐI CÙNG bằng hàm pop
      + Kiểm tra state đã đi qua hay chưa. Nếu chưa đi thì cho vào list visited trạng thái đang xét, kiểm tra đã đến đích chưa, push các trạng thái liền kề state đó vào stack
    
# breadthFirstSearch
  - Tương tự depthFirstSearch, thay vì tạo stack thì ta tạo queue lưu state, ở vòng lặp lấy ra State đầu tiên của queue bằng hàm pop

#  uniformCostSearch
  - Lấy ra trạng thái ban đầu của agent và kiểm tra goal state
  - Tạo list visited lưu các state đã đi qua
  - Tạo hàng đợi ưu tiên lưu state 
  - Push trạng thái gồm tên, đường đi đến trạng thái, chi phí đường đi (cost) và giá trị ưu tiên
  - Tao vòng lặp khi hàng đợi còn phần tử thì duyệt
      + Lấy ra State đầu tiên của hàng đợi gồm tên, đường đi đến trạng thái, chi phí đường đi bằng hàm pop
      + Kiểm tra state đã đến đích hay chưa. Nếu chưa đi thì cho vào list visited trạng thái đang xét, push các trạng thái liền kề state đó gồm tên, đường đi đến trạng thái, chi phí đường đi vào hàng đợi
        * next_state = successor[0]
        * path_to_next_state = path + [successor[1]]
        * cost_to_nextState = cost + successor[2]
        * priority = cost + successor[2]
    
# aStarSearch
  - Tương tự uniformCostSearch, chỉ khác với giá trị ưu tiên được cập nhật bằng cost_next_state + heuristic 
