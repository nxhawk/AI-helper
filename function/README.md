# Auto Start Minesweeper

  Chương trình đơn giản với pyautogui. Giúp bạn tự động chọn (mở) ngẫu nhiên các ô khi bắt đầu game minesweeper. 
  
  Read Document [here](https://pyautogui.readthedocs.io/en/latest/index.html).

## 1. Run terminal
  ![image](https://user-images.githubusercontent.com/92797788/215349866-edce63ca-5fcc-4c22-b8c3-06365ccb2310.png)
  
## 2. How to use
  * 1. Truy cập link web game <a href="https://minesweeperonline.com/" target="_blank">minesweeper</a>
  * 2. Chương trình chỉ hỗ trợ các size màn hình web game ở (100%, 110%, 125%, 150%, 175%), khuyến khích đặt size ở 175% (hay 150%).


     ![image](https://user-images.githubusercontent.com/92797788/215350313-4d88e0a0-c11c-489b-b932-f6b4c1e0bc1d.png)

  * 3. Run terminal như trên.
  * 4. Nhập số ô bạn muốn mở (mặc định 10 lần).
  * 5. Chuyển vào trang web game (trong vòng <b>2s</b> sau khi {run terminal và nhập input}).
  * 6. Chờ chương trình thực thi xong.
  * 7. Nếu muốn dừng chương trình, tại web game ấn tổ hợp phím 'Ctrl'+'+' để dừng.
  * 8. Play game. Done!!!.

## 3. Note
  Khi run code game sẽ tự động bắt đầu lại.
  
  Đảm bảo web game phải full màn hình, board game phải hiển thị đầy đủ không bị che.
  
  Vì chưa thử trên nhiều thiết bị (laptop/desktop) nên có thể sẽ có lỗi xảy ra.
  
  Nếu gặp lỗi thì hãy chạy lại chương trình lần nữa.
  
  Nếu bạn chạy 5->10 lần mà vẫn lỗi thì bạn có thể sửa lại [code](https://github.com/nxhawk/AI-helper/blob/master/function/auto_game.py) để phù hợp với thiết bị của bạn.
  
  Hay có thể do kích thước của image không phù hợp, bạn hãy thay đổi kích thước image cho phù hợp theo [link](https://github.com/nxhawk/AI-helper/tree/master/function/img) với các số 100, 110, 125, 150, 175 là hình ảnh ở kích thước màn hình tương ứng. 
