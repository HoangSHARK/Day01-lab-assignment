# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.
gpt4o_response: Temperature controls the randomness of the model's output, with higher values leading to more diverse responses, while top_p (nucleus sampling) limits the output to the smallest set of words whose cumulative probability exceeds a certain threshold, ensuring more coherent responses.
mini_response: Temperature controls the randomness of the model's predictions, with lower values resulting in more deterministic outputs, while top_p (nucleus sampling) limits the selection of words to a dynamic subset based on cumulative probability, allowing for more diverse outputs.
gpt4o_latency: 3.105522632598877
mini_latency: 1.3678255081176758
gpt4o_cost_estimate: 0.0005333333333333334
---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**
--- Kết quả với Temperature = 0.0 ---
Một sự thật thú vị về Việt Nam là đất nước này có một hệ thống hang động tự nhiên lớn nhất thế giới, đó là hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang động này được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh, nhưng mãi đến năm 2009 mới được công bố rộng rãi sau khi một đoàn thám hiểm người Anh tiến hành khảo sát. Hang Sơn Đoòng có kích thước khổng lồ với chiều dài hơn 5 km, cao 200 m và rộng 150 m, đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang có hệ sinh thái riêng biệt, với rừng cây, sông ngầm và các loài động thực vật độc đáo.
(Độ trễ: 3.83 giây)

--- Kết quả với Temperature = 0.5 ---
Một sự thật thú vị về Việt Nam là đất nước này có một hệ thống hang động rất ấn tượng, trong đó có Hang Sơn Đoòng, được coi là hang động lớn nhất thế giới. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình. Hang này được phát hiện vào năm 1991 bởi một người dân địa phương và sau đó được khám phá kỹ lưỡng hơn bởi các nhà thám hiểm người Anh vào năm 2009. Hang Sơn Đoòng có chiều dài hơn 5 km, cao 200 m và rộng 150 m. Bên trong hang có cả một hệ sinh thái riêng biệt với rừng cây, sông ngầm và các loài động vật đặc hữu. Đây là một điểm đến hấp dẫn cho những người yêu thích khám phá và phiêu lưu.
(Độ trễ: 2.50 giây)

--- Kết quả với Temperature = 1.0 ---
Một sự thật thú vị về Việt Nam là quốc gia này có hệ thống hang động lớn nhất thế giới, được gọi là hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình. Được phát hiện vào năm 1991 và chính thức khảo sát vào năm 2009, hang động này có chiều dài hơn 5 km, cao tới 200 mét và rộng 150 mét ở một số khu vực, đủ lớn để chứa một chiếc Boeing 747. Bên trong hang còn có một hệ sinh thái độc đáo, với rừng nguyên sinh, sông ngầm và thậm chí cả những đám mây tự tạo do sự chênh lệch nhiệt độ. Sơn Đoòng đã thu hút sự chú ý của nhiều nhà thám hiểm và du khách từ khắp nơi trên thế giới, làm cho nó trở thành một điểm đến du lịch mạo hiểm nổi tiếng.
(Độ trễ: 5.84 giây)

--- Kết quả với Temperature = 1.5 ---
Một sự thật thú vị về Việt Nam là quốc gia này có hang động lớn nhất thế giới, đó là Hang Sơn Đoòng. Hang này nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, thuộc tỉnh Quảng Bình. Hang Sơn Đoòng được hình thành khoảng 2-5 triệu năm trước, với kích thước khổng lồ: dài hơn 5 km, cao 200 m và rộng 150 m. Bên trong hang có cả một hệ sinh thái riêng biệt với rừng cây, sông ngầm và các loài động thực vật đặc biệt. Việc khám phá và tham quan hang động này mang đến cho du khách trải nghiệm như bước vào một thế giới khác.
(Độ trễ: 4.56 giây)
**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng dần từ 0.0 đến 1.5, mô hình có xu hướng đa dạng hóa cách diễn đạt và mở rộng các chi tiết so sánh sinh động hơn (như từ việc so sánh với "tòa nhà 40 tầng" ở mức 0.0 sang "chiếc Boeing 747" và "đám mây tự tạo" ở mức 1.0). Tuy nhiên, do prompt mang tính chất hỏi về sự thật khách quan (fact), các mức temperature thấp (0.0 và 0.5) cho cấu trúc câu cực kỳ chặt chẽ và tập trung, trong khi mức 1.5 bắt đầu có dấu hiệu lặp lại các ý cơ bản một cách đơn giản hóa chứ không tăng thêm độ sâu thông tin.
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Em sẽ đặt temperature từ 0.0 đến 0.2 cho chatbot hỗ trợ khách hàng bởi vì hệ thống chăm sóc khách hàng đòi hỏi sự chính xác tuyệt đối, tính nhất quán và độ tin cậy cao khi cung cấp các thông tin về chính sách, giá cả hoặc quy trình dịch vụ của doanh nghiệp. Việc thiết lập temperature gần bằng 0 sẽ ép mô hình luôn lựa chọn những từ ngữ có xác suất cao nhất (mang tính deterministic), triệt tiêu sự ngẫu nhiên ngớ ngẩn và ngăn chặn hoàn toàn tình trạng AI tự "sáng tạo" ra thông tin sai lệch (hallucination) gây ảnh hưởng đến uy tín doanh nghiệp

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> Dựa trên đơn giá ($0.010$ so với $0.0006$ USD trên 1K tokens), GPT-4o đắt hơn GPT-4o-mini đúng 16.67 lần. Với workload 10.5 triệu tokens/ngày, doanh nghiệp phải trả 105 USD/ngày cho GPT-4o nhưng chỉ tốn 6.3 USD/ngày nếu dùng GPT-4o-mini (tiết kiệm gần 3.000 USD/tháng)

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> GPT-4o xứng đáng: Các tác vụ cần lập luận phức tạp, logic chuyên sâu và độ chính xác tuyệt đối như Phân tích báo cáo tài chính doanh nghiệp, Rà soát lỗi mã nguồn (Code Review) hệ thống lớn, hoặc Hỗ trợ chẩn đoán y tế. Những kịch bản này đòi hỏi chất lượng câu trả lời cao nhất vì một sai sót nhỏ có thể gây thiệt hại lớn về kinh tế hoặc vận hành.

GPT-4o-mini tốt hơn: Các tác vụ lặp đi lặp lại với khối lượng dữ liệu khổng lồ nhưng có cấu trúc đơn giản như Phân loại ý định khách hàng (Intent Classification), Trích xuất thông tin thực thể (Entity Extraction), hoặc Tóm tắt lịch sử cuộc gọi/đoạn chat. Việc chọn bản mini giúp tối ưu hóa biên lợi nhuận cực lớn cho doanh nghiệp mà vẫn đảm bảo tốc độ phản hồi nhanh.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất ở các ứng dụng tương tác thời gian thực trực tiếp với con người (như Chatbot, trợ lý ảo, hoặc công cụ viết văn bản dài) nhằm giảm thời gian chờ đợi tâm lý, mang lại trải nghiệm mượt mà bằng cách hiển thị các từ ngay khi chúng được tạo ra. Ngược lại, Non-streaming lại phù hợp hơn cho các tác vụ chạy ngầm (background/batch jobs) không có người đợi trực tiếp như Trích xuất dữ liệu thành cấu trúc JSON, Phân tích sắc thái bình luận hàng loạt, hoặc Gọi API lồng nhau (Chain of agents) — nơi hệ thống chỉ cần kết quả trọn vẹn, chính xác cuối cùng để xử lý các bước logic tiếp theo.

## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
