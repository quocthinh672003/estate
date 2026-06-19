






Văn bản đã dán (1)(4).txt
Tài liệu
bạn là chuyên gia về IT và phân tích exp 10 years, hãy phân tích nội dung trên và giải thích trình bày các func và chuẩn bị những câu hỏi cần để hỏi hiểu rõ hơn nếu cần cần

Tôi đã đọc nội dung. Với góc nhìn BA/SA + Tech Lead 10 năm kinh nghiệm, đây là tài liệu BRD/FRS sơ bộ cho hệ thống BeON Pay gồm các module:

M1: Budget Management

M2: E-Signer

M3: Master Data

M4: Payment Request (PR)

M5: Payment Voucher + MISA Integration

M6: Cash In/Out

M7: Integration & Dashboard

Tài liệu khá chi tiết về nghiệp vụ nhưng còn rất nhiều điểm cần làm rõ trước khi estimate và thiết kế hệ thống.

1. Tổng quan luồng nghiệp vụ
Budget
   ↓
Budget Lock
   ↓
Memo / Contract
   ↓
PR (Payment Request)
   ↓
Accounting Review
   ↓
Approver (DGD/GD/President)
   ↓
PV (Payment Voucher)
   ↓
CFO Approve
   ↓
Bank Transfer
   ↓
MISA Accounting
2. Module M1 - Budget Management
Chức năng chính
M1.01 Budget Master
Quản lý danh mục:

Budget Account

Budget Item

Cost Center

Internal Order (IO)

Ví dụ:

Training Budget
    |
    +-- ABC_HCM
    +-- ABC_HN
    +-- BCD_HCM
=> Giống SAP Internal Order.

M1.02 Budget Planning
Cho phép:

Nhập trực tiếp

Import Excel

Copy năm trước

Workflow:

Member
   ↓
Team Lead
   ↓
DGD
   ↓
Accounting
   ↓
CFO
   ↓
GD
   ↓
Thailand HQ
M1.03 Budget Transfer
Điều chuyển ngân sách:

Marketing
    100M

↓ Transfer 20M

Training
    +20M
Các case:

Team → Team

Budget → Budget

Month → Month

M1.04 Carry Forward
Giữ ngân sách năm cũ.

Ví dụ:

Budget 2025
    Remaining: 100M

Register Carry Forward

2026 PR
    use 100M from 2025
M1.05 Budget Lock
Đây là chức năng cực kỳ quan trọng.

Ví dụ:

Budget = 500M

Lock = 100M

Available = 400M
Sau này PR sẽ consume từ phần lock này.

M1.06 Budget Monitoring
Dashboard realtime:

Planned Budget
Adjusted Budget
Locked Budget
Pending PR
Actual Expense
Remaining Budget
Câu hỏi cần hỏi thêm
Budget Structure
Một Budget có bao nhiêu cấp?

Company
  Department
     Team
        Budget Item
hay

Company
   Cost Center
      Budget Item
Budget versioning?

Budget 2026 v1
Budget 2026 v2
Budget 2026 Final
Có cần không?

Khi Thailand yêu cầu sửa budget:

Có tạo version mới không?

Hay overwrite?

Budget Lock:

Một lock có được dùng cho nhiều PR không?

Ví dụ:

Lock 100M

PR1 = 30M
PR2 = 20M
PR3 = 50M
Lock expire thế nào?

Expire Date?
Auto Unlock?
3. Module M4 - Payment Request
Đây là module phức tạp nhất.

Loại PR
1. Normal PR
Vendor Payment
Employee Reimbursement
2. Advance PR
Advance
     ↓
Spend
     ↓
Settlement
3. Intercompany PR
Chi hộ công ty khác.

Không trừ budget.

Các Rule quan trọng
Rule 1
Invoice > 7 triệu

↓

Procurement Required

Rule 2
Invoice > 35 triệu

↓

3 quotation

Rule 3
Invoice > 200 triệu

↓

Bidding

Rule 4
Certificate

Không có hóa đơn

↓

Budget = Amount × 120%

Ví dụ:

Actual = 100M

CIT = 20M

Budget Consume = 120M
Các câu hỏi phải làm rõ
1.
Một PR có thể thuộc nhiều Cost Center không?

Tài liệu ghi có.

Cần confirm:

1 PR
  Line 1 -> CC A
  Line 2 -> CC B
Approval tính theo:

tổng PR
hay

từng line

2.
Currency?

Chỉ VND?

Hay:

VND
USD
THB
EUR
3.
VAT Handling

Ví dụ:

Amount = 110M
VAT = 10M
Expense = 100M
Budget trừ:

100M ?
110M ?
Tài liệu nói VAT không trừ budget.

Cần confirm toàn bộ flow.

4.
Invoice OCR

Có dùng:

Google Vision

Azure Form Recognizer

OpenAI Vision

hay OCR tự build?

5.
PR Draft

Draft có lock budget không?

Tài liệu đang mâu thuẫn:

M1 ghi:

Lock khi tạo Budget Lock
M4 ghi:

Submit PR -> tạm lock
Cần clarify.

4. Module M5 - Payment Voucher
Flow
PR Approved
      ↓
Generate PV
      ↓
Accounting
      ↓
CFO
      ↓
Bank
MISA Integration
Có 2 chiều:

Push
BeON
   ↓
MISA
Pull
MISA
   ↓
BeON
Các câu hỏi kỹ thuật
1.
MISA version?

Ví dụ:

MISA SME

AMIS Accounting

MISA Enterprise

API khác nhau.

2.
Sync frequency?

Realtime
5 mins
Hourly
Nightly
3.
Nếu MISA sửa:

Account Code
Description
Posting Date
BeON có update lại không?

4.
Nếu MISA xóa voucher?

Xử lý thế nào?

5. Module M2 - E-Signer
Có 2 loại:

Internal
Memo
Proposal
Request
E-Contract
Digital Signature
Câu hỏi cần hỏi
1.
Nhà cung cấp ký số?

Ví dụ:

MISA eSign

FPT CA

VNPT CA

Viettel CA

2.
Ký theo:

USB Token
Remote Signing
HSM
3.
Có timestamp không?

4.
PDF sau ký có cần chứng thực pháp lý không?

6. Module M6 - Cashflow
Đây là phần có nhiều rủi ro kỹ thuật.

Bank Integration
Tài liệu ghi:

Export file
Upload lên Internet Banking
chứ không phải chuyển khoản trực tiếp.

Câu hỏi
Ngân hàng nào?

Vietcombank

BIDV

HSBC

SCB

UOB

Mỗi ngân hàng có format riêng.

Email Parsing
M6.06

Đọc email báo tiền vào ra.

Câu hỏi
Email lấy từ đâu?

shared mailbox?
Protocol?

IMAP
Microsoft Graph
Gmail API
Một ngày bao nhiêu mail?

Để estimate AI parsing.

7. Kiến trúc kỹ thuật tôi đề xuất
Từ tài liệu này, tôi sẽ chia thành:

Budget Service
PR Service
Approval Service
PV Service
Accounting Service
Notification Service
Integration Service
Master Data Service
Các integration:

MISA
E-Sign
Bank
Thinkspace
HR
Taxi
Travel
Email
Những câu hỏi quan trọng nhất cần hỏi khách hàng ngay
Nhóm Budget
Budget hierarchy chính thức?

Budget versioning có không?

Budget Lock dùng nhiều PR được không?

Lock expire thế nào?

Nhóm PR
Approval dựa trên tổng PR hay từng line?

Có multi-currency không?

VAT có trừ budget không?

Draft PR có lock budget không?

Nhóm MISA
Đang dùng phiên bản MISA nào?

MISA có API license chưa?

Sync realtime hay batch?

Nhóm E-Sign
Dùng nhà cung cấp ký số nào?

Token hay remote signing?

Nhóm Bank
Danh sách ngân hàng sử dụng?

Có API Open Banking không hay chỉ upload file?

Nhóm Data Migration
Có bao nhiêu năm dữ liệu budget cần migrate?

Có migrate PR/PV lịch sử không?

Dung lượng chứng từ hiện tại bao nhiêu GB?

Đây là 18 câu hỏi tôi sẽ hỏi đầu tiên trong buổi Grooming/Discovery trước khi bắt đầu thiết kế Solution Architecture hoặc estimate effort.


PR, VAT Handling là gì

Trong tài liệu này:

1. PR là gì?
PR = Payment Request (Đề nghị thanh toán)

Đây là chứng từ nhân viên tạo để xin công ty thanh toán một khoản chi phí.

Ví dụ:

Trường hợp 1: Thanh toán nhà cung cấp
Công ty mua laptop Dell
Giá: 30 triệu

↓
Nhân viên tạo PR
↓
Sếp duyệt
↓
Kế toán xử lý
↓
Công ty chuyển tiền cho Dell
Trường hợp 2: Hoàn tiền cho nhân viên
Anh A tự bỏ tiền mua vật tư

10 triệu

↓
Anh A tạo PR
↓
Đính kèm hóa đơn
↓
Duyệt
↓
Công ty trả lại 10 triệu cho anh A
Trong hệ thống này có 3 loại PR
PR Thông thường
Thanh toán NCC
Hoàn tiền nhân viên
PR Advance
Tạm ứng

Ví dụ:

Xin tạm ứng 20 triệu đi công tác

↓

Chi thực tế

↓

Khai báo quyết toán (settle)
PR Chi hộ
SCG VN trả tiền giúp công ty khác

Ví dụ:

SCG VN chi hộ SCG Thailand

↓

Sau này thu lại
Không trừ ngân sách SCG VN.

2. VAT Handling là gì?
VAT = Thuế Giá Trị Gia Tăng (VAT)

Handling = cách hệ thống xử lý VAT.

Ví dụ hóa đơn:

Tiền hàng: 100 triệu

VAT 10%: 10 triệu

Tổng thanh toán: 110 triệu
Câu hỏi cần làm rõ
Khi làm PR:

Ngân sách bị trừ bao nhiêu?

Cách 1
Trừ cả VAT

Budget = 110 triệu
Cách 2
Không trừ VAT

Budget = 100 triệu
Vì VAT được khấu trừ thuế sau này.

Trong tài liệu của bạn
M4.01 có ghi:

VAT không được trừ vào budget (là thuế được khấu trừ)

=> Nghĩa là:

Tiền hàng: 100 triệu
VAT: 10 triệu

Budget giảm: 100 triệu
chứ không phải 110 triệu.

Ví dụ thực tế
Budget Marketing:

500 triệu
Làm PR:

Chi phí quảng cáo: 200 triệu
VAT: 20 triệu
Khi duyệt:

Tổng tiền trả NCC:
220 triệu

Budget còn lại:
500 - 200

= 300 triệu
không phải:

500 - 220

= 280 triệu
Vì sao tôi đặt câu hỏi "VAT Handling"?
Vì rất nhiều hệ thống ERP xử lý khác nhau:

Hệ thống	Budget trừ VAT?
SAP	Thường không
Oracle	Cấu hình được
MISA	Tùy nghiệp vụ
Odoo	Tùy cấu hình
Nên dù tài liệu hiện tại có ghi "VAT không trừ budget", vẫn cần hỏi khách hàng thêm:

VAT đầu vào có luôn được khấu trừ không?

Có trường hợp VAT không được khấu trừ không?

VAT nước ngoài (FCT) xử lý thế nào?

Certificate + CIT 20% có cộng vào budget hay không?

Đây là những câu hỏi BA/SA thường phải xác nhận với kế toán trước khi thiết kế database và logic tính toán.


thông tin tổng hợp dài dòng khó nhìn quá, các câu q&a cũng trình bày khó nhìn, và bạn nói gì tôi cũng chưa hiểu thì sao tôi dám hỏi họ, họ hỏi ngược lại thì tôi trả lời sao??

Đúng. Nếu bạn chưa hiểu nghiệp vụ mà đi hỏi khách hàng theo kiểu BA thì rất dễ bị "vặn ngược".

Sai lầm lớn nhất của BA mới là:

Hỏi vì checklist bảo phải hỏi
thay vì:

Hiểu nghiệp vụ trước
↓
Biết hệ thống đang làm gì
↓
Biết rủi ro ở đâu
↓
Mới hỏi
Ví dụ PR là gì?
Đừng nghĩ tới hệ thống.

Nghĩ đơn giản như đời thực.

Bạn đi ăn với khách hàng.

Bạn bỏ tiền túi:

2 triệu
Sau đó muốn công ty trả lại.

Bạn phải:

1. Chụp hóa đơn
2. Ghi lý do
3. Xin sếp duyệt
4. Kế toán chuyển tiền
Cái đơn bạn tạo chính là:

PR = Payment Request
= Đề nghị thanh toán
Tại sao phải có Budget?
Ví dụ phòng Marketing được cấp:

100 triệu/năm
Đã chi:

90 triệu
Còn:

10 triệu
Bạn tạo PR:

Chi quảng cáo
20 triệu
Hệ thống phải chặn:

Budget còn 10
PR đòi chi 20

=> Không cho submit
Đó là lý do Budget liên kết PR.

Budget Lock là gì?
Ví dụ công ty chuẩn bị ký hợp đồng:

100 triệu
Nhưng chưa thanh toán.

Nếu không khóa:

Budget còn 100 triệu
Người khác nhìn thấy:

Ồ còn 100 triệu
Rồi họ tiêu tiếp.

Sau 1 tháng:

Hợp đồng 100 triệu
+
Người khác tiêu 80 triệu

= Vượt ngân sách
Nên phải:

Lock 100 triệu
Tức là:

Đánh dấu:

100 triệu này đã có người giữ chỗ
Giống đặt vé máy bay.

VAT là gì?
Ví dụ hóa đơn:

Tiền hàng:
100 triệu

VAT:
10 triệu

Tổng:
110 triệu
Câu hỏi là:

Budget trừ bao nhiêu?

Case A

Trừ 110 triệu
Case B

Trừ 100 triệu
Tài liệu đang ghi:

VAT không trừ budget
Nghĩa là:

Budget chỉ giảm 100 triệu
Vậy tại sao BA phải hỏi?
Không phải để hỏi cho có.

Mà để tránh dev sai.

Ví dụ:

Khách hàng nói:

VAT không trừ budget
Nhưng sau đó kế toán bảo:

Có vài loại VAT không được khấu trừ.
Lúc này hệ thống sẽ thành:

VAT được khấu trừ
→ Không trừ budget

VAT không được khấu trừ
→ Có trừ budget
Nếu không hỏi từ đầu:

Dev xong
↓
UAT fail
↓
Làm lại
Với tài liệu này, trước mắt bạn chỉ cần hiểu 5 khái niệm
Khái niệm	Hiểu đơn giản
Budget	Hạn mức tiền được phép chi
Budget Lock	Giữ chỗ ngân sách
PR	Đơn xin thanh toán
PV	Phiếu chi sau khi PR được duyệt
MISA Sync	Đẩy dữ liệu sang phần mềm kế toán
Nếu bạn hiểu chắc 5 cái này thì đọc được khoảng 70% tài liệu.

Tôi có thể làm tiếp theo kiểu dễ hiểu hơn:

M1 Budget
↓ giải thích như người mới

M4 PR
↓ giải thích như người mới

M5 PV
↓ giải thích như người mới

MISA
↓ giải thích như người mới

Approval Flow
↓ vẽ sơ đồ
và chỉ ra:

Chức năng nào khó nhất

Chức năng nào dễ estimate

Chức năng nào khách hàng chắc chắn sẽ đổi yêu cầu nhiều lần

Những câu nào BA bắt buộc phải hỏi vì nếu không hỏi thì dev không làm được

theo kiểu "người mới vào dự án vẫn hiểu". Đây thường là cách hiệu quả hơn khi chuẩn bị đi họp grooming/discovery.

tổng hợp lại nội dung thông tin

"No.
STT" "Module ID
Mã Module" "Module (VI)
Tên Module (VI)" Module (EN) "Function
Chức năng" "Sub-Function
Chức năng con" Description / Mô tả chi tiết Package "BAP Notes
Ghi chú BAP" "Customer Feedback
Feedback KH" "Desired Process
Quy trình mong muốn" "Current Process
Quy trình hiện tại" "Pain Points
Vấn đề giải quyết" "Users
Đối tượng sử dụng" "Priority
Mức ưu tiên" "Status
Trạng thái" "Owner
Phụ trách" "Notes
Ghi chú"
M1.01 M1 Quản lý Ngân sách Budget Management Budget Management Danh mục Budget "- Danh mục Budget account, budget name (có thể tham chiếu budget ứng với tài khoản kế toán nào khi nào PR)

Common Assumption: Điểm đến công tác (Trong nước/ nước ngoài), Perdiem, Hotel rate, Airticket rate, transportation, Public relation,…

Danh mục IO (Internal Order): là danh mục mà các Team tao project chi tiết (nếu cần) để theo dõi từng project

Danh mục loại PR ko cần làm bước khóa budget: như chi phí ăn uống, các khoản chi ký hợp đồng dài hạn nhưng chi hàng tháng,...

Danh sách có thể Filter/ defaute được
có phân quyền loại budget nào thì user nào được xem (bảo mật thông tin)" "Ví dụ IO: Team có Tổng ngân sách ""62787_Training"" là 1 tỷ, chi tiết cho các lớp ABC_HCM, ABC_HN, BCD_HCM, BCD_HP thì Team có thể mở:

62787_Training: 1 tỷ

62787_0001: Training ABC_HCM: 200tr

62787_0002: Training ABC_HN: 300tr

62787_0003: Training BCD_HCM: 250tr

62787_0004: Training BCD_HN: 250tr"
M1.02 M1 Quản lý Ngân sách Budget Management Budget Management Lập ngân sách "Cho phép người dùng lập ngân sách theo kỳ (năm) theo 3 cách:
• Điền form trực tiếp trên hệ thống (có thông tin Assumption, giá đơn vị, ... kế toán mà kế toán đã cập nhật)
• Export/ Import format file Excel
• Copy ngân sách từ kỳ trước để chỉnh sửa
Hỗ trợ cấu trúc ngân sách theo Department / Team / Cost Center / Budget Item.

Assign function:

Team lead sẽ chỉ định 1 hoặc nhiều người được phân quyền điền budget

Team lead review và chỉnh sửa -> submit" NEW Cần xác định danh sách template Assumption SCG VN đang dùng để tích hợp hoặc cung cấp file mẫu tương ứng. "- SCG VN gởi file excel hiện tại đang dùng để BAP tham khảo

File Assumption, kế toán sẽ cập nhật thông tin giá đơn vị (thay đổi theo kỳ), user chỉ điền khối lượng, hệ thống sẽ tự động tính toán ngân sách liên quan.

Khi làm budget trên format, do format có nhiều item nên user dễ bị rối, nên user có thể tắt bớt thông tin budget ko liên quan để dễ làm

Format có cột ghi chú điền thônng tin, nếu user muốn xem thì có thể mở/ tắt trường này." "Hàng năm, tới kỳ lập ngân sách, kế toán sẽ gởi email cho các Team lead về việc lập ngân sách, bao gồm timeline -> Các team lead sẽ vô hệ thống BeONpay để giao nhiệm vụ cho member nào, làm phân nào của ngân sách -> Các member làm xong sẽ submit cho Teamlead -> Team lead tổng hợp, điều chỉnh trực tiếp trên file mà member đã submit (có lịch sử chỉnh sửa và báo cho member biết, file đã được chỉnh sửa chỗ nào) -> Team lead submit cho DGD review, DGD có thể chỉnh sửa trực tiếp or Back lại cho Team lead để chỉnh sửa (Approve/ Reject/ Back) -> Sau khi GDG duyệt xong -> Kế toán nhận thông tin, tổng hợp số liệu, dựa trên số liệu tổng này làm report FS, có chi tiết thông tin, ước tính doanh thu trong năm - budget trong năm, để ra báo cáo toàn công ty -> Gởi cho CFO review (Approve/ Reject/ Back) -> CFO submit to GD (Approve/ Reject/ Back) -> dựa trên file này, KT sẽ làm report file excel theo format bên Thái, gời email report cho bên Thái -> Bên Thái review qua email, nếu bên Thái yêu cầu chỉnh sửa thì GD sẽ unlock budget đã duyệt trên hệ thống BeON và trả về cho bước Kế Toán được quyền chỉnh sửa ngân sách trên BeONpay và làm lại report -> KT gởi cho CFO review -> CFO gởi lại cho GD

Trường hợp bên Thái họ yêu cầu điều chỉnh ngân sách thì KT có thể được quyền chỉnh sửa (theo chỉ đạo của CFO/GD) file budget trên BeONpay mà các Team đã nộp cho phù hợp với quy định bên Thái, việc thay đổi này hệ thống sẽ thông báo cho các Team biết)" Hàng năm, tới kỳ lập ngân sách, kế toán sẽ gởi email cho các Team lead về việc lập ngân sách, timeline và Form excel file để làm -> Các Team lead tự làm nội bộ với team member, ra được file ngân sách chung của Team -> Gởi email cho DGD review chỉnh sửa,...gởi lại cho Team lead -> Team lead gởi email file budget của Team cho Kế toán -> KT tổng hợp từng file excel vào file của toàn công ty, KT thêm các thông tin doanh thu của từng khách hàng, và các thông tin khác để làm bộ báo cáo (BS, PL) ngân sách năm -> KT gởi report cho CFO review/ chỉnh sửa -> KT gởi file cho GD review/ chỉnh sửa -> Sau khi GD approve, KT làm report theo format bên Thái để gởi email qua bên Thái để review/ chỉnh sửa (trường hợp bền Thái yêu cầu điều chỉnh thì KT trao đổi lại với CFO và GD để điều chỉnh cho phù hợp), khi bên Thái ko yêu cầu chỉnh sửa và đã chấp nhận file thì budget sẽ là budget được duyệt chính thức để sử dụng trong năm. (KT là người bấm bút confirm budget để dùng chính thức) "- Làm budget thủ công, dễ sai sót công thức.

Tổng hợp nhiều file con, dễ gây thiếu sót, mất thời gian nhiều để kiểm tra

Nhiều file chỉnh sửa, lâu ngày không biết file nào là file được duyệt cuối cùng (user phải hỏi kế toán check)

Thông tin tham khảo của những năm trước (thực tế dùng so với ngân sách) phải hỏi kế toán làm thủ công" "- User: được quyền nhập thông tin, lưu nháp, chỉnh sửa trước khi submit

Team lead: được thêm quyền giao nhiệm vụ cho user nào làm, chỉnh sửa trên file mà user submit, được Approve/ reject/Back

DGD: là người được thêm quyền chỉnh sửa trên file được nhận duyệt, quyền Approve/ reject/Back

CFO: Chỉnh sửa/ Approve/ reject/Back

GD: Approve/ reject/Back

President: Approve/ reject/Back"
M1.03 M1 Quản lý Ngân sách Budget Management Budget Management Điều chỉnh & Chuyển ngân sách "Cho phép điều chỉnh ngân sách sau khi đã được duyệt:
• Bổ sung thêm ngân sách cho một hạng mục/phòng ban
• Gộp ngân sách từ nhiều hạng mục/ phòng ban
• Điều chuyển ngân sách giữa các hạng mục trong cùng phòng ban
• Điều chuyển ngân sách từ tháng này qua tháng khác trong năm của cùng phòng ban
• Điều chuyển ngân sách giữa các phòng ban (cần duyệt riêng)
• Lưu lịch sử mỗi lần điều chỉnh (người thực hiện, thời gian, lý do)" NEW "Cần thiết kế màn hình config DOA cho phần này linh hoạt để Admin điều chỉnh % theo từng cấp khi có thay đổi policy.
Luồng duyệt chuyển ngân sách giữa phòng ban cần là một approval flow riêng biệt." "- Hệ thống phân cấp duyệt chuyển/gộp ngân sách theo quy định:
• Điều chuyển trong phòng ban: Team Lead duyệt ≤10%, DGD duyệt ≤50%, GD duyệt >50%
• Điều chuyển giữa phòng ban: DGD duyệt <10%, GD duyệt <50%, President duyệt ≥50%
(Tỷ lệ % tạm thời, sẽ xác nhận chính xác khi lên hệ thống)

Xin tăng budget phải dược president phê duyệt" Khi user làm PR nhận thấy thiếu ngân sách -> User sẽ vô chỗ ngân sách (hệ thống có thể link từ chỗ tạo PR) để tạo đơn xin chuyển ngân sách từ đâu sang đâu, lý do chuyển -> Hệ thống sẽ nhận diện mức chuyển trong phạm vi nào của Policy để xác định người duyệt cho lệnh điều chỉnh này. -> User submit để được duyệt -> Người duyệt có quyền Approve/ Reject/ Back -> Sau khi budget được duyệt chuyển, user vô làm PR lại Khi thiếu ngân sách, các Team trao đổi nội bộ với Team mình để linh hoạt điều chỉnh trong ngân sách tổng -> Tự chuyển qua ngân sách tương đương (miễn ko vượt số tổng) - Không theo dõi được đã chuyển ngân sách như thế nào -> làm cho việc lập ngân sách cho các kỳ sau ko có đủ thông tin để điều chỉnh cho phù hợp với thực tế "- Requester

Approvers (theo luồng Policy)"
M1.04 M1 Quản lý Ngân sách Budget Management Budget Management Kết chuyển ngân sách "Xử lý trường hợp ngân sách của năm trước chưa sử dụng hết hoặc chi phí phát sinh trong năm nay nhưng thuộc ngân sách năm cũ:
• User có thể chọn ngân sách năm cũ khi tạo PR trong năm hiện tại
• Hệ thống ghi nhận và phân biệt rõ nguồn ngân sách (năm hiện tại vs năm trước)
• Báo cáo thể hiện rõ khoản nào đang dùng ngân sách năm trước" NEW Cần thiết kế trường 'Năm ngân sách' riêng biệt với 'Năm tài chính' trên PR. Report cần có filter/group theo năm ngân sách. Đối với ngân sách của kỳ trước muốn dùng cho kỳ này thì phải đăng ký với kế toán để giữ ngân sách (nếu ko đăng ký thì hệ thống sẽ khóa ko cho dùng ngân sách kỳ cũ) KT bấm nút thông báo hạn đăng ký giữ ngân sách kỳ trước cho các Team trên BeON (có hạn đăng ký) -> Các Team tạo request giữ ngân sách (khóa ngân sách) + đính kèm chứng từ theo quy định làm evidence -> Hệ thống ghi nhận và khóa budget lock theo hạn đăng ký -> Năm sau: User chọn ngân sách đã khóa của năm cũ khi tạo PR thanh toán Cuối năm, các Team sẽ báo cho kế toán về thông tin ngân sách của năm nay nhưng chi tiền vào năm sau kèm theo danh sách và các chứng từ có liên quan để chứng minh là ngân sách thuộc năm nay nhưng thanh toán ko kịp trong năm nên xin giữ để năm sau làm thanh toán -> KT dựa trên thông tin này đễ giữ ngân sách "- Phụ thuộc vào email thủ công, dễ bỏ sót

Không có bằng chứng audit trail cho kết chuyển" "- Requester

Approvers (theo luồng Policy)"
M1.05 M1 Quản lý Ngân sách Budget Management Budget Management Khóa ngân sách (Budget Lock) "Chức năng cho phép user xin khóa trước một khoản ngân sách trước khi ký hợp đồng hoặc thực hiện thủ tục mua hàng:
• User nhập thông tin xin khóa (có thể link thông tin từ Memo): hạng mục, số tiền, lý do, thời hạn dự kiến dùng
• Team Lead xác nhận → hệ thống sinh mã khóa budget duy nhất
• Khi tạo PR thanh toán cho hợp đồng này, user nhập mã khóa budget → hệ thống tự động trừ vào số budget đã khóa
• Budget đã khóa nhưng không dùng hết → có thể unlock để trả lại
• Budget Report thể hiện được: Tổng NS → Đã dùng → Đang khóa → Chưa làm PR (chênh lệch giữa đã khóa và đã làm PR)
(khi làm memo hệ thống link thông tin qua chức năng làm khóa ngân sách)" NEW "Cần thiết kế:

Form xin khóa budget (số tiền, lý do, thời hạn, hạng mục)

Màn hình quản lý danh sách budget đã khóa (theo trạng thái: Pending/Locked/Partially Used/Fully Used/Unlocked)

Logic trừ budget khi PR được duyệt (từ khoản đã khóa)

Logic unlock và hoàn trả số dư" "- Muốn xin khóa budget thì chứng từ phải có là Memo đính kèm. Khi sếp ký hợp đồng cũng biết rằng còn budget cho khoản này

Có chỗ link tới làm Memo để tạo Memo (Phần mềm nội bộ or ký số)

Số tiền xin khóa và số tiền sau đó thực tế dùng sẽ được linh hoạt +/- 10%. Vì dụ xin khóa 100tr nhưng thực tế dùng là 110tr, thì lúc làm các PR cho hạng mục này khoản tẳng 10tr ko cần phải xin khóa thêm, mễn ngân sách trong đó còn thì vẫn submit PR được.

Budget Report có thể show được khoản trước khi làm PR và sau khi làm PR chênh lệch chỗ nào chưa làm PR để user theo dõi." "Sau khi Memo được duyệt (trên BeON) -> User tạo đơn xin khóa: hạng mục, số tiền, lý do, thời hạn -> Submit → Người duyệt Approve/ Reject/ Back → Hệ thống sinh mã Budget Lock duy nhất
Khi user cần khóa ngân sách-> User sẽ vô chỗ ngân sách để tạo đơn xin khóa ngân sách nào, lý do gì -> User submit để được duyệt -> Người duyệt có quyền Approve/ Reject/ Back -> Sau khi budget được khóa, user tiến hành làm hợp đồng và các chứng từ liên quan (làm bên ngoài BeON) -> Khi có phát sinh các PR liên quan, user sẽ chọn mã budget lock này để submit PR.

Lưu ý: Một số PR lớn hơn 7tr mà ko cần làm khóa budget như chi phí ăn uống, các hợp đồng ký 1 lần nhưng phát sinh PR hàng tháng,... thì có chỗ chọn Item và phải đăng ký danh mục trước, đến khi làm PR thì chỉ việc chọn hợp đồng phù hợp là được" Các NV họ tự quản lý ngân sách thủ công trên file của họ "- User không biết ngân sách còn lại → khó lập kế hoạch dự án

Rủi ro ký hợp đồng vượt ngân sách" "- Requester

Approvers (theo luồng Policy)"
M1.06 M1 Quản lý Ngân sách Budget Management Budget Management Theo dõi & Cảnh báo ngân sách "Màn hình theo dõi tình hình sử dụng ngân sách theo thời gian thực:
• Hiển thị 4 chỉ số: Planned Budget / Adjusted Budget / Actual Expense / Remaining Budget
• Thêm chỉ số: Locked Budget (đang bị khóa chờ làm PR) và Pending PR (đã làm PR chờ duyệt)
• Cảnh báo khi: vượt ngân sách (màu đỏ) hoặc gần chạm ngưỡng (% threshold, cấu hình được)
• Cho phép xem theo nhiều chiều: theo Department / Team / Cost Center / Budget Item / Năm ngân sách" NEW Cột 'Adjusted Budget' cần được thêm mới so với thiết kế ban đầu. Tính năng export cần hỗ trợ định dạng .xlsx (không chỉ .csv). "- Có việc điều chỉnh ngân sách nên hệ thống cần theo dõi và so sánh đủ thông tin: Planned Budget / Adjusted Budget / Actual Expense / Remaining Budget.
'- Có việc budget năm trước mà chi trong năm nay nên có thông tin này bên dưới budget năm nay.
'- Có việc xin khóa budget để ký hợp đồng / mua hàng / Draft PR nên cần có thông tin này để user biết ngân sách nào đang xin khóa / khóa chỗ nào / Budget nào đã dùng.
-' Cần đảm bảo số dư hiển thị chính xác tại màn hình làm PR để tránh bị Deny. (thông tin budget hiện ngay chỗ line làm PR, ko phải link vô report xem)
'- Bổ sung cảnh báo ngưỡng ngân sách bằng màu sắc.
'- Report data xuất được file Excel (không chỉ CSV)." "Khi user làm PR chỗ chọn thông tin budget, hệ thống sẽ hiển thị số tiền remaining ngay bên cạnh mã Bugdet. Ví dụ user chọn Budget 64283_Entertainment fee, thì số tiền còn lại của budget này sẽ hiện ngay bên cạnh.
Đối với PR có mã lock budget thì chỗ budget này sẽ hiển thị 2 thông tin: số còn lại của phần lock, số còn lại của Team" Hệ thống link vô bảng ngân sách, để user dò rồi back lại
M1.07 M1 Quản lý Ngân sách Budget Management Budget Management Danh sách ngân sách "Màn hình danh sách tổng hợp các mục ngân sách:
• Filter theo: năm, kỳ, department, team, cost center, trạng thái duyệt
• Group/sort linh hoạt
• Hiển thị trạng thái từng mục: Draft / Submitted / Approved / Locked / Adjusted
• Phân quyền xem theo vai trò (xem chi tiết tại sub-function Phân quyền)" NEW Cần phân quyền xem theo phòng ban chặt chẽ. Riêng budget lương cần có tag/category đặc biệt để chỉ HR role mới có quyền xem. Thiết kế nhân viên phòng nào chỉ được xem phòng đó. Nếu 1 Team Lead quản lý nhiều phòng thì sẽ cấp quyền tương ứng. Budget liên quan đến lương thì chỉ HR mới được xem. "- Các user thấy được budget của phòng ban mình: Các xem được linh hoạt tùy theo ý user muốn xem full format hay chỉ xem những item nào có phát sinh số tiền thì show ra thôi

Admin thấy được toàn bộ của các Team, lọc được xem từng Team.

Admin có thể phân quyền cho 1 user có thể xem budget của các phòng khác để, trường hợp user làm PR chung cho nhiều phòng ban.

Team lead và cấp cao hơn của từng phòng ban cũng có thể tự mình cấp quyền cho user khác phòng có thể xem được 1 vài item budget của phòng mình để họ thấy budget để làm PR có liên quan. Ví dụ: Tú làm Admin, Tú thường có các PR thanh toán vé máy bay, hotel cho các phòng ban,... thì Tú được cấp quyền vộ xem budget của vé máy bay, hotel của các phòng để dễ làm PR" "- Các user thấy được budget của phòng ban mình, các item của format thể hiện ra hết, có tiền hay ko có tiền đều list ra

Admin thấy được toàn bộ của các Team, lọc được xem từng Team"
M1.08 M1 Quản lý Ngân sách Budget Management Budget Management Quy trình phê duyệt ngân sách "Luồng phê duyệt ngân sách theo chuỗi:
User tạo budget -> Reviewer 1 (Head of Department) duyệt -> reviewer 2 (DGD)→ Gửi Accounting review → AI hỗ trợ tạo báo cáo tổng hợp → Gửi CFO → GD phê duyệt hoặc yêu cầu chỉnh sửa → Finalize & Lock
Trạng thái vòng đời: Draft → Submitted → Accounting Reviewed → CFO -> GD Reviewed → Approved/ Rejected → Locked
(Manager có thể edit trực tiếp -> approve....) - chỉ thông báo cho user thay đổi chỗ nào

Permission và approval flow sẽ được thiết kế cụ thể trong quá trình phát triển" NEW Cần confirm với SCG VN số cấp duyệt cụ thể và ai là người có quyền BOD review tại từng công ty. "Các luồng phê duyệt khác nhau:

Lập ngân sách

Điều chỉnh/ chuyên ngân sách

Tăng ngân sách

Lock ngân sách" "Thiếu minh bạch trong quá trình phê duyệt
Không có audit trail về ai đã duyệt khi nào"
M1.09 M1 Quản lý Ngân sách Budget Management Budget Management Báo cáo ngân sách "Bao gồm 2 loại màn hình:

Dashboard trực quan:
• Tổng ngân sách theo Department / Team / Cost Center
• Tỷ lệ sử dụng ngân sách (actual/budget %)
• Tình trạng phê duyệt
• Theo dõi ngân sách điều chỉnh và khóa ngân sách
• Action Dashboard: tổng hợp đơn/request cần phê duyệt

Reports chi tiết (export CSV và Excel):
• Budget vs Actual
• P&L theo ngân sách
• Lịch sử điều chỉnh ngân sách
• Báo cáo cho BOD / HO (PDF / Excel)" NEW Bổ sung tracking khóa ngân sách vào dashboard. Tất cả nút export cần hỗ trợ cả .xlsx và .csv. "'- Chỉ cần đủ data -> User tự dùng AI phân tích

Data cần có thêm theo dõi ngân sách điều chỉnh và khóa ngân sách (như mô tả ở sub-function 1.4 và 1.5).
Report data xuất được file Excel (không chỉ CSV)."
M1.10 M1 Quản lý Ngân sách Budget Management Budget Management Phân quyền & Audit Log "• Phân quyền theo vai trò: xem / tạo / chỉnh sửa / duyệt ngân sách
• Phân quyền đặc biệt: budget lương chỉ HR role mới xem được
• Audit log ghi nhận: người tạo, người duyệt, thời điểm, nội dung thay đổi cho mọi thao tác trên ngân sách" NEW Budget lương cần được đánh tag riêng (category = 'Salary') và kiểm soát quyền xem ở cả màn hình list, detail lẫn export. "Rủi ro lộ thông tin nhạy cảm (lương, chi phí)
Không truy vết được ai đã thay đổi dữ liệu"
M1.11 M1 Quản lý Ngân sách Budget Management Budget Management Tích hợp Payment Process "Sau khi ngân sách được Finalize & Lock, hệ thống tự động mở cổng cho Payment Process sử dụng ngân sách này.
• Payment Request chỉ được tạo khi đã có ngân sách tương ứng đã được duyệt
• Khi ngân sách bị điều chỉnh (tăng/giảm/chuyển) trong quá trình sử dụng → Payment Process cập nhật số dư ngân sách tương ứng theo thời gian thực" NEW Cần thiết kế cơ chế sync 2 chiều giữa Budget module và Payment Process: mỗi khi budget bị điều chỉnh phải cập nhật lại Remaining Budget hiển thị trên PR đang pending. Trong quá trình dùng budget có sự điều chỉnh so với budget ban đầu thì Payment Process cũng sẽ phải cập nhật tương ứng.
M2.01 M2 Ký điện tử E-Signer Ký điện tử Danh mục/ phân quyền người dùng "Đăng nhập bằng tài khoản nội bộ trên BeON

Phân quyền theo vai trò: Người ký, Người duyệt, Quản trị viên

Quản lý danh sách người dùng: thêm, sửa, vô hiệu hóa tài khoản

Tài liệu ký có 2 loại: 1. Internal_loại ký nội bộ như Memo (ko cần ký số), loại 2. E-contract_là các chứng từ cần ký số điện tử giữa 2 bên như hợp đồng (giống như ký điện tử Misa)"
M2.02 M2 Ký điện tử E-Signer Ký điện tử Quy trình ký "Tải lên tài liệu cần ký (PDF)/ Hay có format trên hệ thống sẵn

Mỗi loại sẽ có số thứ tự theo dõi khác nhau: Ví dụ: Internal_001, E-contract_001

Có chỗ cho attached document có liên quan khi trình ký

Xem trước tài liệu trong trình duyệt trước khi ký

Luồng duyệt của các chứng từ Internal khác nhau: Luồng duyệt tài liệu Internal theo policy của Công ty; Luồng duyệt E-contract bắt buộc phải người đại diện pháp luật lý

Ví dụ luồng duyệt (luồng duyệt chính thức sẽ trao đổi khi làm) : Requester -> Line manager -> Approver -> Legal Representative

Chỗ luồng duyệt có thể có chức năng ủy quyền (Ví dụ người đại diện pháp luật ký giấy ủy quyền cho DGD ký đại diện pháp luật thay cho GD trong khoảng thời gian cụ thể, thì hệ thống cũng có thể chuyển ủy quyền ký số cho DGD đó)

Chứng từ sau khi ký có thể link qua Budget Management để làm lock budget và link qua PR để làm Payment Request"
M3.01 M3 Danh mục dùng chung Master Data / Category Danh mục/ Category Tạo & Quản lý Danh mục "Danh mục cost center (phân loại bước duyệt)

Danh mục tổng (có filter) (Danh mục phải khớp mã số ID với phần mềm kế toán)

Danh mục nhà cung cấp: Cho phép user tạo theo rule (link tới phần mềm Misa để user tạo)
Danh mục mới, user có thể tự làm, nhưng chỉ được dùng 1 lần khi làm PR, thông tin nhà cung cấp mới này sẽ được lưu draft, hệ thống thông báo cho kế toán, kế toán vào check để duyệt vào list danh sách chính thức để dùng cho những lần phát sinh sau

Danh mục khách hàng -> kế toán tạo

Danh mục nhân viên theo dữ liệu HR trên BeON (oganization charge của BeON)

Danh mục Cost element / cost budget/ code account KT/ cost report/ tập hợp chi phí

Role & Permission (approval, view, take actions...) - thảo luận trong quá trình xây hệ thống"
M4.01 M4 Đề nghị Thanh toán (PR) Payment Request (PR) Payment Process Tạo & Quản lý Payment Request "Cho phép tạo và quản lý yêu cầu thanh toán với đầy đủ phân loại và rule nghiệp vụ.
A. CÁCH TẠO PR:
• Tạo thủ công từ các nguồn ngoài BeON
• Tạo tự động từ dữ liệu sẵn có trên BeON (lương, thuế, trip business): hệ thống trigger tạo draft → thông báo user → user review & submit
• PR định kỳ: hợp đồng thường xuyên → đến ngày quy định hệ thống tự tạo draft và thông báo user
• Hệ thống suggest nội dung song ngữ (VI/EN) để giảm nhập tay
-> Khi chụp, upload hoặc chọn chứng từ khi làm PR, hệ thống có thể tự động quét lấy dữ liệu vô trường tương ứng

B. PHÂN LOẠI PR — 3 loại:
(1) PR Thông thường: đề nghị chi cho NCC hoặc NV khi có đủ hóa đơn chứng từ → trừ ngân sách ngay

Số tiền dưới 7tr, có hóa đơn chứng từ đầy đủ -> scan hóa đơn, hệ thống quét hóa đơn, đề xuất nội dung theo từng line, số hóa đơn, ngày hóa đơn,... -> user review -> submit

Số tiền từ 7 triệu trở lên nhưng nằm trong danh mục loại trừ thủ tục mua hàng (như: chi phí ăn uống, đào tạo, tài trợ,... ) thì user làm PR submit như bình thường.

Số tiền trên 7 triệu nhưng không nằm trong danh mục loại trừ thủ tục mua hàng thì có 2 loại:

Hợp đồng thường xuyên (là hợp đồng ký 1 lần nhiều tháng, nhiều năm nhưng phát sinh chi mỗi tháng, mỗi kỳ) thì user sẽ chọn trong danh mục hợp đồng -> hệ thống cho phép làm PR.

Hợp đồng phát sinh từng lần, thì user sẽ chọn mã khóa ngân sách -> hệ thống cho phép làm PR.
(Xem chi tiết mở mục D)

(2) PR Advance (Tạm ứng & Thẻ tín dụng Công ty):

Tạm ứng tiền: tạm ứng cho NV, chưa trừ NS khi chi (nhưng phải khóa ngân sách khi advance được duyệt) — chỉ trừ khi NV settle. Nếu còn treo advance chưa settle mà muốn advance thêm → hệ thống cảnh báo, NV phải kê lý do, cấp cao hơn duyệt, highlight giải trình. NV nhập ngày dự kiến settle → hệ thống nhắc; trễ 1 tuần cảnh báo lên cấp trên, càng trễ leo cấp càng cao (thời gian clear nằm trong policy của Công ty, ko được quá thời gian này)

Luồng Settle Advance là workflow con của PR Advance:

NV nhận advance → chi tiêu thực tế

Đến hạn settle → NV vào màn hình Settle Advance

Kê khai từng khoản thực chi:
Có HĐ → nhập bình thường
Không có HĐ → tạo Certificate + tính 20% CIT

Tính toán: thực chi < advance → hoàn trả phần dư; thực chi > advance → tạo PR bổ sung -> Khi clear advance nếu số tiền lớn hơn advance thì dùng thêm budget và submit clear advance cho sếp duyệt

Submit → KT review → Approved → TRỪ NGÂN SÁCH theo chứng từ settle

Advance status chuyển sang: Settled

Tạm ứng bằng thẻ Tín dụng Công ty: Kê khai thông tin khi giao thẻ cho nhân viên.
Công ty mở cấp thẻ tín dụng cho một số nhân viên sử dụng theo hạn mức tín dụng được cấp. NV nào được cấp thẻ tín dụng, kế toán sẽ cài thông tin vào, hàng tháng hệ thống sẽ nhắc người giữ thẻ settle Credit card trong tháng, kế toán có thể vô upload sao kê chi tiêu trong tháng của NV để NV biết số cần settle theo đúng với bank statement. Có chức năng trình duyệt xin được sử dụng thẻ tín dụng từng lần (áp dụng cho nhân viên), attached memo có liên quan. Sau khi chi xong thì phải attached document liên quan lên hệ thống để cuối kỳ tổng hợp chứng từ settle.

Xin duyệt trước khi thực hiện hoạt động: như chi phí ăn uống (tiếp khách), giao tế,... -> Khi user có kế hoạch tiếp khách (ăn uống), user sẽ vô chức năng này để xin sếp duyệt trước đi. Ví dụ: NV A có kế hoạch tiếp đoàn khách -> NV A vô chức năng này để tạo Request -> chọn các thông tin liên quan như Tier khách, bao nhiêu người, ngân sách mỗi người bao nhiêu,... (các thông tin này admin sẽ cài đặt trước theo Rule hoặc theo Guideline của từng công ty) -> NV A đi tiếp khách -> NV A laim chi phí thì vô chức năng này để claim và link với PR

(3) PR Chi hộ: chi hộ cho công ty khác trong tập đoàn, không thuộc NS SCG VN → không trừ NS. Tính tổng tiền gồm VAT -> Chỗ chi hộ sẽ theo dõi theo hợp đồng chi hộ, sẽ được KT khai báo khi có phát sinh hợp đồng chi hộ. Mỗi lần làm PR chi hộ, sẽ hiển thị thông tin hợp đồng và tổng số tiền chi hộ, hệ thống cũng theo dõi số tiền này, chi tới đâu thì sẽ giảm tới đó, realtime như theo dõi ngân sách. Nếu chi cao hơn khoản cam kết trong hợp đồng thì user request tăng khoản chi hộ và làm thủ tục tăng tương ứng. User có thể advance để chi tiêu cho hoạt động chi hộ, khi user đề nghị advance thì sẽ tính theo hợp đồng chi hộ, chứ ko khóa ngân sách của SCG Việt Nam.

Certificate: chứng từ xin duyệt chi phí không có hóa đơn thuế (ví dụ: ăn uống tại quán không xuất HĐ). Kê người bán, địa chỉ, nội dung, lý do. Theo dõi tổng số tiền Certificate của từng user; nếu tổng lớn → cấp cao hơn duyệt + cảnh báo rủi ro -> Certificate ko phải là loại PR riêng mà nó là 1 thủ tục sẽ phát sinh nếu khi làm các PR khác (PR thông thường, Clear advance, PR chi hộ) mà có khoản chi không có hóa đơn, chứng từ thì sẽ chọn để làm Certificate này trong PR đó luôn.

C. NHẬP TỪNG LINE CHI PHÍ:
• Mỗi PR nhập nhiều line: dòng chi phí theo từng phòng ban + 1 dòng VAT riêng biệt. 1 PR có thể có nhiều hóa đơn
• 1 PR có thể chọn nhiều budget / nhiều phòng ban (VD: admin thanh toán vé máy bay cho nhiều phòng → chọn budget từng phòng tương ứng)
• Hiển thị Budget còn lại ngay tại cột kế bên khi nhập từng line (cả người nhập và người duyệt đều thấy)
• VAT không được trừ vào budget (là thuế được khấu trừ)
• Khi submit PR (chưa được duyệt) → budget được tạm khóa tương ứng -> khi duyệt xong thì trừ budget chính thức
• Khi draft PR: hệ thống tự động mapping tài khoản chi phí dựa trên budget + cost center → KT chỉ cần review khi qua PV

LƯU Ý CHUNG KHI LÀM CÁC PR:

Khi User chụp/ scan/ upload chứng từ hệ thống quét hóa đơn/ chứng từ số hóa đơn, ngày hóa đơn, nhà cung cấp, số tiền, nội dung đề xuất... vô từng line PR -> user review, chỉnh sửa -> submit

Chỗ attached file chứng từ đính kèm, có thể đính kèm nhiều file, mỗi line PR có thế attached chứng từ liên quan đến line thanh toán đó để dể theo dõi (nếu attached thiếu file thì hệ thống cho phép attached thêm sau khi duyệt

Các khoản chi có Certificate hệ thống sẽ trừ budget thêm 20% CIT do không có hóa đơn thì Công ty phải loại chi phí khi tính thuế CIT (Certificate + tính 20% CIT) -> Trên mục khi làm Certificate có cảnh báo thông tin này, giao diện sếp duyệt cũng có tổng thông tin này để cảnh báo (gồm thông tin Certificate (20% CIT) phát sinh của PR này và thông tin tích lũy YTD theo phòng ban.

Có chức năng copy PR cũ để làm PR mới

Đối với những thanh toán chưa có hóa đơn (sau khi thanh toán vendor mới xuất hóa đơn), cho phép user chọn vào ô ""bổ sung hóa đơn sau"". Sau khi tiền đi sẽ nhắc nhở user attach bổ sung hóa đơn. Tương tự với những payment tài trợ, yêu cầu user attach bổ sung biên bản xác nhận tài trợ. Chỉ cho phép user bổ sung thêm tài liệu chứ không được thay đổi bất kì dữ liệu nào trong PR/PV. -> KT cũng có quyền mở thêm yêu cầu user bổ sung chứng từ trong trường hợp user bổ sung thiếu chứng từ

D. KIỂM TRA NGƯỠNG HÓA ĐƠN (HĐ) & CHỨNG TỪ BẮT BUỘC:
• Không có HĐ → hệ thống cảnh báo bắt buộc có Certificate
• Hóa Đơn ≤ 7 triệu → đủ chứng từ liên quan là được như hóa đơn,...
• HĐ > 7tr–35tr → tối thiểu 2 bảng so sánh giá + Memo duyệt chọn đơn vị (mã khóa budget)
• HĐ > 35tr–200tr → tối thiểu 3 bảng so sánh giá + Memo duyệt chọn đơn vị (mã khóa budget)
• HĐ > 200tr → chứng từ Bidding (mã khóa budget)
• Ngoại lệ: 1_HĐ > 7tr nhưng là Hợp Đồng dài hạn (đã làm thủ tục ban đầu) → có danh sách lý do pass thủ tục; khi submit hệ thống hiển thị dòng remark cảnh báo để người duyệt lưu ý -> chọn list trong hợp đồng. 2_trên 7tr mà nằm danh mục ko cần qua thủ tục mua hàng thì được cho làm PR: chi phí ăn uống, .....
• HĐ ≥ 5tr (gồm VAT) chi cho NV SCG VN → bắt buộc có chứng từ không tiền mặt (Giấy ủy quyền / UNC)
Ghi chú: Số tiền chỉ mang tính tham khảo, khi policy thay đổi thì admin có thể điều chỉnh số tiền cho phù hợp với Policy mới
Khi upload hóa đơn lên, hệ thống nhận diện được giá trị tổng của các hóa đơn trong cùng 1 ngày của hóa đơn của 1 nhà cung cấp (theo MST) nếu trên 5tr thì hệ thống cảnh báo. TRánh xuất hóa đơn trong cùng 1 ngày có giá trị trên 5tr (gồm VAT)

E. KIỂM TRA BUDGET — RULE VALIDATION:
• Nếu không đủ budget → hệ thống chặn submit, hiển thị thông báo yêu cầu user qua module Budget xin chuyển/tăng NS → sau khi được duyệt mới quay lại submit PR
• Nếu PR vượt ngưỡng Procurement → phải có mã số Budget Lock trước, hoặc phải nằm trong danh sách lý do cho phép

F. SAU KHI PR ĐƯỢC DUYỆT:
• Cho phép đính kèm thêm chứng từ và ghi chú bổ sung (link với PV tương ứng)
• Hệ thống tự động tạo PV từ PR đã duyệt" CUSTOM "Cần thiết kế kỹ:

Màn hình nhập PR phải hiển thị budget còn lại theo từng line realtime

Logic kiểm tra ngưỡng HĐ phải chạy tự động khi user nhập giá trị HĐ

Danh sách lý do ""pass thủ tục"" cần được config bởi Admin

Cần confirm với SCG VN template chứng từ chuẩn theo từng loại PR

Logic tạm khóa budget khi lưu Draft cần đồng bộ với Budget Lock ở module Budget

[Nhắc tạm ứng quá hạn]
Logic nhắc advance quá hạn là background job chạy định kỳ (KHÔNG chỉ trigger khi user tạo PR mới). Cần thiết kế notification engine riêng — xem Function 9 Notification Center.

[Gom PR+PV trên 1 màn hình]
PR và PV là 2 entity độc lập về data và logic. Về UX: PV được hiển thị nhúng trong màn hình detail của PR theo dạng Tab (Tab 1: Thông tin PR / Tab 2: Payment Voucher / Tab 3: Lịch sử Audit). Người dùng thấy toàn hành trình trên 1 màn hình. PV vẫn có ID riêng, luồng duyệt riêng (KT viên → KT trưởng → CFO)."
M4.02 M4 Đề nghị Thanh toán (PR) Payment Request (PR) Payment Process Phê duyệt Payment Request theo DOA "Luồng phê duyệt đa cấp, linh hoạt cấu hình theo DOA của SCG VN.

A. CẤU HÌNH BƯỚC DUYỆT:
• Hệ thống cho phép cấu hình tối đa N bước duyệt (flexible, không giới hạn cứng) -> Bước duyệt sẽ được thiết kế theo Rule của Cost Center (New folow) Ex: 2360-10000/ 2360-11000/ 2360-10100/.... flow sẽ được thiết kế trong quá trình phát triển
• Hiện tại SCG VN có tối đa 4 bước; thiết kế để dễ mở rộng khi có thêm công ty khác trong SCG group
• Các bước chưa dùng → tắt; khi cần mở rộng → bật lên không cần dev thêm
• Admin điều chỉnh ngưỡng tiền theo DOA khi có thay đổi policy

Lưu ý có bước review chứng từ của bộ phận kế toán (bước KT sau khi Team lead duyệt) trước khi lên DGD/ GD duyệt

B. MA TRẬN DUYỆT THEO DOA:
• PR Thông thường ≤4,000 USD: DGD phụ trách bộ phận duyệt
• PR Thông thường >4,000 USD: DGD + GD duyệt
• Chi phí tiếp khách/quà tặng: DGD ≤300 USD / GD ≤1,500 USD / President >1,500 USD
• Chi phí giao tế: GD ≤3,000 USD / President >3,000 USD
• Chi phí tài trợ: GD ≤1,500 USD / President >1,500 USD
• PR Advance ≤600 USD: DGD / 600–3,000 USD: DGD+GD / >3,000 USD: President
• PR Chi hộ & Certificate: flow duyệt như PR Thông thường

Action: Save Draft, Submit, Cancel, Recall

Khi user submit mà chưa ai duyệt thì user có thể thể Recall (khi user bấm recall thì người duyệt ko thấy nữa) / Delete
PR được duyệt nhưng KT chưa submit PV, requester muốn hủy PR thì có thể hủy, trường hợp PV đã được duyệt thì requester phải làm đề nghị trên hệ thống đề nghị KT hủy PV (nếu KT chưa làm thanh toán qua ngân hàng thì đc)

Requester có 3 action khi tạo PR:

Cancel -> thoát, không lưu gì

Save draft -> lưu nháp, chưa gửi đi đâu

Submit -> gửi PR lên hệ thống, chờ approval duyệt

Sau khi submit, nếu 1st approval chưa duyệt, requester có thêm 2 action: delete và recall

action delete: Toàn bộ thông tin PR đi vào ""màn hình huỷ"" (soft delete, không mất data), approval không thể thao tác với PR đó nữa

action recall:
Màn hình approval: PR bị xoá khỏi danh sách chờ duyệt
Màn hình requester: được mở lại toàn bộ form để chỉnh sửa
Sau khi chỉnh, có 2 lựa chọn:

Save draft -> lưu nháp, chưa gửi lại

Re-submit -> gửi lại, hệ thống chạy lại toàn bộ logic duyệt theo thông tin mới

C. KIỂM TRA CHỨNG TỪ KHI DUYỆT:
• Khi người duyệt action Approve → hệ thống tự động kiểm tra điều kiện chứng từ theo loại PR và ngưỡng HĐ
-> Người duyệt yêu cầu thêm gì thì note và Return lại cho requester

D. GIAO DIỆN PHÊ DUYỆT:
• Highlight key info để người duyệt nắm nhanh (ví dụ có Certificate -> giải thích cho người duyệt rủi ro cho cty khi duyệt sẽ thêm 20% CIT, có CP trên 5tr NV chi hộ, FCT nộp thêm trong trường hợp...)
• Hiển thị Budget còn lại của phòng ban / hạng mục tương ứng
• Hiển thị lý do policy được áp dụng: ""Case này được duyệt vì thỏa điều kiện A/B/C trong policy""
• 3 action: Approve / Reject / Return (Return = trả về để chỉnh sửa, không phải reject hẳn)

E. RESEND NHẮC DUYỆT:
• Sau X ngày (configurable) người duyệt chưa action → hệ thống tự động gửi nhắc
• Người tạo PR có thể chủ động bấm ""Resend"" để gửi lại thông báo nhắc
• Giới hạn resend thủ công: tối đa Y lần/ngày (tránh spam — configurable)
• Logic resend được quản lý tập trung tại Function 9 — Notification Center" CUSTOM "1. Cần thiết kế màn hình config DOA linh hoạt: Admin nhập ngưỡng tiền + cấp duyệt cho từng loại PR
2. Nút Return cần có ô nhập lý do bắt buộc
3. Màn hình duyệt mobile-friendly vì sếp hay duyệt trên điện thoại
4. Cần confirm toàn bộ DOA matrix với SCG VN trước khi dev

[BỔ SUNG] Chức năng Resend: cần config ngưỡng số ngày chờ và số lần resend tối đa. Logic gửi thông báo delegate sang Notification Center (F9)."
M4.03 M4 Đề nghị Thanh toán (PR) Payment Request (PR) Payment Process Danh sách & Export Payment Request "• Màn hình danh sách tất cả PR với filter: theo loại, trạng thái, phòng ban, người tạo, ngày, ngưỡng tiền
• Group và sort linh hoạt
• Xem chi tiết từng PR
• Export PDF: tính năng độc lập cho phép xuất PR dưới dạng PDF để review hoặc lưu hồ sơ
• Hiển thị lịch sử thay đổi trạng thái của từng PR (audit trail)
Thêm trường dữ liệu và bộ lọc theo Tên người nhận tiền/Đối tác để phục vụ tra cứu nhanh khi Kế toán hoặc Sếp truy vấn." CUSTOM Export PDF cần có định dạng chuẩn, bao gồm đầy đủ thông tin PR, danh sách chứng từ đính kèm và lịch sử duyệt.
M4.04 M4 Đề nghị Thanh toán (PR) Payment Request (PR) Payment Process Quản lý Certificate "Certificate là chứng từ nội bộ để xin phê duyệt các khoản chi thực tế không lấy được hóa đơn thuế VAT từ người bán (VD: ăn uống tiếp khách tại quán không xuất được HĐ).

A. VỊ TRÍ TRONG LUỒNG PR:
Certificate được nhúng trực tiếp trong luồng tạo PR — khi user nhập line chi phí không có HĐ → hệ thống hiển thị option chọn Certificate ngay tại đó → user khai báo thông tin Certificate trên cùng form.

B. THÔNG TIN BẮT BUỘC TRÊN CERTIFICATE:
• Tên người bán / đơn vị cung cấp
• Địa chỉ người bán
• Nội dung khoản chi (mua gì / chi cho việc gì)
• Số tiền thực chi
• Lý do người bán không xuất được hóa đơn thuế
• Thông tin người đề nghị

C. TÍNH TOÁN 20% CIT:
• Chi phí không có HĐ bị tính thêm 20% CIT (Corporate Income Tax — thuế TNDN)
• Form Certificate hiển thị:

Số tiền thực chi: X

20% CIT phát sinh: X × 20%

Tổng budget bị trừ: X × 120%
• Hệ thống tự động tính và hiển thị để người duyệt nắm rõ tổng ảnh hưởng ngân sách

D. LUỒNG XỬ LÝ:
User chọn Certificate trong PR → khai báo thông tin → hệ thống tính 20% CIT
→ Xác định cấp duyệt dựa trên tổng tích lũy (xem phần E) -> không cần luồng duyệt riêng cho Certificate, user kê khai ngay trong PR, khi sếp duyệt PR đồng thời sếp đã duyệt Certificate trong PR này (có thể export DPF file Certificate này và thông tin người duyệt), lúc sếp duyệt PR có hiển thị thông tin Certificate bao nhiêu, CIT bao nhiêu,...
-> sinh Mã Certificate nằm trong line PR tương ứng

E. LOGIC LEO THANG CẤP DUYỆT THEO TỔNG TÍCH LŨY:
• Hệ thống theo dõi tổng số tiền tất cả Certificate đã duyệt của từng user theo kỳ
• Nếu tổng tích lũy vượt ngưỡng → Certificate tiếp theo tự động yêu cầu cấp duyệt cao hơn
• Người duyệt thấy cảnh báo rủi ro: tổng Certificate user đã xin từ đầu kỳ, số lần, xu hướng

F. QUẢN LÝ DANH SÁCH CERTIFICATE:
• Màn hình danh sách: filter theo user, phòng ban, trạng thái, kỳ
• Trạng thái vòng đời: Draft → Submitted → Approved → Rejected → Used (đã gắn vào PR)
• Validate: mã Certificate phải hợp lệ (đã duyệt, chưa dùng, đúng user/phòng ban)
• Số tiền PR không được vượt số tiền ghi trên Certificate" CUSTOM "1. Certificate có thể gắn vào nhiều PR không, hay chỉ 1 PR? -> khi user làm PR có lìn nào có Certificate thì kê khai vô trực tiếp trên PR.
2. Certificate có thời hạn hiệu lực sau khi duyệt không? -> Certificate được duyệt chung với PR nên được dùng liền chung với PR."
M4.05 M4 Đề nghị Thanh toán (PR) Payment Request (PR) Payment Process Báo cáo Certificate "Màn hình báo cáo riêng cho Certificate, phục vụ kiểm soát rủi ro và phân tích xu hướng chi phí không hóa đơn.

A. CÁC CHIỀU PHÂN TÍCH:
• Theo nhân viên: tổng tiền Certificate, số lần, tần suất theo kỳ, trending tăng/giảm
• Theo phòng ban: tổng tiền Certificate / tổng chi phí phòng ban (tỷ lệ %), so sánh giữa các phòng
• Theo kỳ: tháng / quý / năm — so sánh kỳ này vs kỳ trước
• Top ranking: NV / phòng ban có Certificate cao nhất

B. CHỈ SỐ HIỂN THỊ:
• Tổng tiền Certificate (trước 20% CIT)
• Tổng budget thực tế bị trừ (sau 20% CIT)
• Số lượng Certificate đã duyệt / đã từ chối
• Tỷ lệ Certificate / tổng chi phí (%)
• Tần suất: số Certificate / tháng

C. MỤC ĐÍCH SỬ DỤNG:
• Người duyệt dùng để ra quyết định leo cấp
• Ban lãnh đạo dùng để kiểm soát rủi ro chi phí không hóa đơn
• KT dùng để theo dõi ảnh hưởng thuế (CIT)
• Export Excel để phục vụ báo cáo thuế

Certificate có report data cho từng phòng ban, nhân viên nào phòng ban nào có số tiền Certificate nhiều, tỷ lệ bao nhiêu, tần suất thế nào." CUSTOM Report Certificate cần được thiết kế như 1 dashboard riêng (không chỉ là filter của danh sách Certificate). Dữ liệu report cần include cả phần 20% CIT để KT theo dõi ảnh hưởng thuế.
M5.01 M5 Phiếu chi & Tích hợp phần mềm Payment Voucher & Software Quản lý Payment Voucher "Phiếu chi được tạo tự động từ PR đã duyệt đã thể hiện KT (kế toán viên, KTT) review rồi, qua PV thì form sẽ tự động thể hiện phòng kế toán đã ký rồi, chỉ còn bước CFO duyệt đồng ý cho chi tiền.

A. TẠO PV:
• Hệ thống tự động tạo PV từ PR được duyệt, kế thừa toàn bộ thông tin
• KT chỉ được chỉnh sửa phần hạch toán và nội dung — KHÔNG được sửa số tiền / budget / cost center (trước khi CFO duyệt)
-> PV nào duyệt xong, thông tin Ck ngân hàng sẽ chờ chi, kế toán dowload list chi này để upload lên lên ngân hàng để làm UNC.
-> KT tạo UNC làm thanh toán trên bank -> hệ thống thông báo cho CFO duyệt trên bank -> KT upload UNC vô PV (link với PR để user thấy được UNC này)
• Số chứng từ kế toán (tương ứng với phần mềm KT) phải hiển thị trên PV để KT tra cứu
• Gắn PV với: Payment Request, Cost Center

B. VALIDATE DỮ LIỆU TRƯỚC HẠCH TOÁN:
• Validate logic số liệu
• Chuẩn hóa dữ liệu BeON theo format MISA trước khi đẩy sang
• Khóa chỉnh sửa sau khi validate thành công
-> hỏi lại: Nếu đã record sang phần mềm kế toán thì khi sửa trên phần mềm kế toán thì dữ liệu có tự động chỉnh lại trên BeONpay?

C. PHÊ DUYỆT PV -> chỉ cần thêm bước CFO phê duyệt (phòng KT đã duyệt ở bước PR rồi, qua form PV cũng sẽ thể hiện phòng KT đã duyệt và CFO)

D. UX — HIỂN THỊ PV NHÚNG TRONG PR DETAIL:
• Về UX: PV được hiển thị nhúng trong màn hình detail PR dưới dạng Tab

Tab 1: Thông tin PR (người nhập, các bước duyệt)

Tab 2: Payment Voucher (tự động sinh sau khi PR Approved —> PV đã được duyệt rồi -> KT thanh toán trên bank -> lock)

Tab 3: Lịch sử / Audit trail
• Khi PR Approved → Tab 2 tự động kích hoạt và hiển thị PV đã được phòng KT duyệt.
• Người dùng không cần chuyển màn hình để theo dõi toàn bộ hành trình

E. TỰ ĐỘNG THÊM TRƯỜNG PHÂN TÍCH TRÊN PV:
• PV tự động điền các trường: Cost element, Service, Khách hàng tương ứng
• Logic mapping: budget + cost center từ PR → gợi ý Cost element; hợp đồng/KH liên quan → gợi ý Service
• KT có thể chỉnh sửa các trường này (không phải read-only như số tiền)

F. RESEND NHẮC DUYỆT NGÂN HÀNG:
• sau khi KT làm lệnh thanh toán trên bank -> chọn các PV đã làm UNC bên bank -> gởi thông báo cho các cấp trên vô ngân hàng duyệt....
• KT viên có thể chủ động Resend
• Logic quản lý tại Function 9 — Notification Center" CUSTOM "1. Cần lock các field số tiền / budget / cost center trên màn hình PV (chỉ read-only)
2. Số chứng từ KT cần được sinh tự động theo format chuẩn SCG VN
3. Cần confirm format số chứng từ với KT của SCG VN

[BỔ SUNG - UX Tab] PR và PV quản lý riêng về data. UX hiển thị PV nhúng trong tab của PR detail để tiện approve 1 lần." SCG Việt Nam, phòng kế toán và Finance chung nên gộp bước duyệt của phòng kế toán khi làm PR ở trên luôn. Tức là khi user làm PR gởi cho Team lead review rồi duyệt -> Phòng kế toán (KT, KTT) duyệt nếu bổ sung gì thì return lại cho user sửa -> Sau khi phòng KT duyệt thì mới gởi lên GDG hoặc GD duyệt theo Policy. Như vậy phòng KT sẽ ko phải trình duyệt PV nữa, mà chỉ cần CFO duyệt là sẽ có PV hoàn chỉnh. (Điều này đáp ứng cho những công ty lớn, tách bạch phòng kế toán và Finance, phòng kế toán duyệt PR, phòng Finance duyệt PV chi tiến)
M5.02 M5 Phiếu chi & Tích hợp phần mềm Payment Voucher & Software Hạch toán & Đồng bộ MISA "Sau khi PV được duyệt hoàn tất trên BeON → đẩy sang MISA để hạch toán chính thức.

LUỒNG ĐÃ XÁC NHẬN VỚI KH:
PV approved trên BeON → BeON đẩy dữ liệu sang MISA dưới dạng draft voucher → KT kiểm tra và post lên GL bên MISA → Sync-back về BeON: trạng thái, mã chứng từ MISA, ngày ghi sổ, nội dung hạch toán đã chỉnh sửa. (-> cần làm rõ quy trình lại với BAP)

CHUYỂN TIỀN:
• Không dùng MISA để thực hiện chi tiền
• BeON tạo file danh sách chuyển tiền theo format chuẩn từng ngân hàng → user download → upload lên internet banking

2-WAY SYNC — LƯU Ý KỸ THUẬT QUAN TRỌNG:
MISA là hệ thống kế toán của bên thứ 3 — BeON không kiểm soát được hành vi của MISA. Toàn bộ logic sync phải được xây dựng và xử lý hoàn toàn ở phía BeON:

• BeON → MISA (push):

BeON chủ động đẩy dữ liệu PV sang MISA qua API

Cần xử lý: retry khi MISA không phản hồi, timeout handling, error log

• MISA → BeON (sync-back):

MISA không chủ động notify BeON khi có thay đổi

BeON phải tự polling định kỳ (scheduled job) để kiểm tra trạng thái bên MISA

Hoặc: KT bấm ""Sync từ MISA"" thủ công trên màn hình PV để pull trạng thái mới nhất

Kết hợp cả 2: polling cuối ngày tự động + sync thủ công khi cần ngay

• Conflict resolution:

Nếu cả BeON và MISA đều thay đổi cùng 1 field: BeON giữ làm master

Số tiền tổng là READ-ONLY tuyệt đối — không bị ghi đè bởi bất kỳ sync nào

Các field hạch toán (tài khoản Nợ/Có, diễn giải) MISA được phép override về BeON

• Reconciliation cuối ngày:

Job tự động so sánh toàn bộ PV giữa BeON và MISA

Phát hiện chênh lệch → cảnh báo KT trưởng xử lý thủ công" NEW "ĐIỀU CHỈNH QUAN TRỌNG theo feedback KH:

Luồng: PV duyệt xong mới đẩy MISA (không phải từ PR)

Bỏ ""liên kết MISA để chuyển tiền"" → tạo file upload bank

RỦI RO KỸ THUẬT
• MISA là hệ thống ngoài, không có webhook → BeON phải tự chạy task background để lấy thông tin về và đồng bộ vào hệ thống, không có sync realtime
• Cần nghiên cứu MISA API spec phiên bản KH đang dùng: endpoint, auth method, rate limit"
M5.03 M5 Phiếu chi & Tích hợp phần mềm Payment Voucher & Software Phân quyền & Audit Log "• Phân quyền theo vai trò trong Payment Process:

Nhân viên: tạo PR

Team Lead / phòng Kế toán/ DGD / GD / President: phê duyệt PR theo DOA
• Audit log ghi nhận toàn bộ: người tạo, người duyệt, thời điểm, nội dung thay đổi, địa chỉ IP" NEW Cần confirm danh sách role đầy đủ với SCG VN, đặc biệt trường hợp 1 người kiêm nhiều role.
M6.01 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Quản lý chi tiền (Phiếu chi) "Tổng hợp và thực hiện các khoản chi sau khi PV đã được duyệt hoàn tất: -> sau khi kế toán làm lệnh chuyển tiền qua ngân hàng có lệnh chuyển tiền thành công thì KT sẽ upload UNC này vô từng PV, user cũng sẽ thấy được UNC này sau khi KT upload
• Hệ thống trigger tạo phiếu chi từ PV đã duyệt
• Tập hợp danh sách phiếu chi chờ thực hiện, filter theo phòng ban / loại chi / ngày
• Tạo danh sách chuyển tiền (file chuẩn theo format từng ngân hàng) để user download và upload lên internet banking
• Thông báo qua email/notification cho người yêu cầu khi tiền đã được chi hoàn tất
-> PV là phiếu chi chính, các khoản chi khác như phí ngân hàng thì KT tự hạch toán vô phần mềm -> Hỏi lại BAP cho rõ chỗ này cách làm tự động" CUSTOM "ĐIỀU CHỈNH theo feedback KH: Bỏ tính năng liên kết MISA để chi tiền.
Thay bằng: tạo file danh sách chuyển tiền theo format chuẩn của từng ngân hàng.
Cần xác nhận với SCG VN đang dùng những ngân hàng nào và format file upload tương ứng."
M6.02 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Quản lý thu tiền & Công nợ "Theo dõi việc thu tiền từ khách hàng và quản lý công nợ:
• Kiểm tra hạn mức: SCG VN chỉ áp dụng hạn mức ngày nợ (≤30 ngày), không có hạn mức tiền nợ → cảnh báo khi khách hàng nợ quá số ngày quy định
• Phiếu thu được tạo khi khách hàng thực sự trả tiền qua ngân hàng (không tạo sớm hơn)
• Theo dõi: khách hàng nào trả trễ, trễ bao nhiêu ngày. Các khung nợ: 0–30 Days, 31–60 Days, 61–90 Days, >90 Days
• KT cập nhật lý do trễ tiền khi liên hệ khách hàng
• Đẩy thông tin lên report realtime" NEW "ĐIỀU CHỈNH theo feedback KH:

Bỏ logic check hạn mức tiền nợ → thay bằng check hạn mức ngày nợ

Phiếu thu chỉ tạo khi có tiền về ngân hàng (trigger từ bank notification)

Cần thiết kế trường ghi chú lý do trễ tiền để KT cập nhật" "SCG VN không có hạn mức tiền nợ, chỉ có hạn mức ngày nợ, thường công nợ không quá 30 ngày.
Phiếu thu phát sinh khi khách hàng trả tiền qua ngân hàng."
M6.03 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Kế hoạch xuất hóa đơn cho KH "Sub-function mới theo yêu cầu SCG VN — quản lý luồng doanh thu từ đầu:
• Quản lý danh sách khách hàng
• Liên kết khách hàng với hợp đồng tương ứng
• Lập kế hoạch xuất hóa đơn cho từng khách hàng trong năm (theo kỳ: tháng/quý/milestone)
• Đến ngày xuất hóa đơn theo kế hoạch → hệ thống API qua phần mềm xuất HĐ điện tử để tạo draft HĐ → thông báo user review → user ký điện tử → phát hành
• Theo dõi: khách hàng nào chưa trả tiền, trễ bao nhiêu ngày → KT liên hệ và cập nhật lý do" NEW "Cần thiết kế:

Module quản lý Khách hàng + Hợp đồng

Lịch xuất Hợp đồng (calendar view) theo từng KH

Cơ chế trigger tạo draft HĐ điện tử qua API MISA" Doanh thu nên đi từ quản lý khách hàng → hợp đồng → kế hoạch xuất hóa đơn cho từng khách hàng trong năm. Đến ngày xuất hóa đơn thì hệ thống sẽ API qua phần mềm xuất hóa đơn để tạo draft hóa đơn. Có chức năng theo dõi việc trả tiền của khách hàng, khách nào trả tiền trễ, trễ bao nhiêu ngày → KT sẽ liên hệ KH và cập nhật lý do trễ tiền.
M6.04 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Xuất hóa đơn điện tử "Flow xuất hóa đơn điện tử cho khách hàng:

Từ BeON: nhập đầy đủ thông tin người nhận hàng

User bấm xuất hóa đơn

BeON gọi API sang MISA (hoặc phần mềm HĐ điện tử)

Nhà cung cấp thông tin điện tử (bên thứ 3) kiểm tra hóa đơn

Phát hành hóa đơn → gửi HĐ cho KH
Quản lý quy trình invoice: trạng thái, lịch sử phát hành, tra cứu" NEW
M6.05 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Cashflow & Quản lý tiền gửi ngân hàng "Theo dõi nguồn tiền tổng thể:
• Hiển thị số dư từng tài khoản ngân hàng để ban lãnh đạo quyết định điều chuyển tiền

• Theo dõi tiền gửi tiết kiệm: số tiền, kỳ hạn, lãi suất, ngày đáo hạn
• Chức năng làm Memo xin duyệt mở tài khoản tiết kiệm (có form mẫu chuẩn)
• Kiểm tra Policy tiền gửi: hiển thị thông tin thực tế so với quy định trong Policy (số tiền thực tế gởi trong State bank, Private bank so với Policy)

QUẢN LÝ THẺ TÍN DỤNG CÔNG TY (Corporate Card) -> Chức năng này nằm song mục Advance ở PR
• Quản lý danh sách thẻ: số thẻ, chủ thẻ, hạn mức chi tiêu, chu kỳ sao kê
• NV khai báo chi phí từ thẻ: nhập từng khoản chi + đính kèm chứng từ

Có HĐ → xử lý bình thường

Không có HĐ → Certificate + tính 20% CIT
• Tất toán thẻ: NV submit bảng kê → KT review → Approved → trừ ngân sách
• Nhắc tất toán: xem Function 9 — Notification Center (9.2)" NEW "Sub-function MỚI hoàn toàn theo feedback KH — không có trong file gốc.
Cần thiết kế:

Kết nối API ngân hàng để lấy số dư realtime (hoặc nhập thủ công nếu ngân hàng không có API)

Module quản lý tiết kiệm với các trường: ngân hàng, số tiền, kỳ hạn, lãi suất, ngày đáo hạn

Template Memo mở TK tiết kiệm

Policy checker: so sánh thực tế với quy định nội bộ

Cần confirm danh sách ngân hàng SCG VN đang có tài khoản

VẤN ĐỀ KỸ THUẬT
Tính năng hiển thị số dư tài khoản phụ thuộc hoàn toàn vào API mà từng ngân hàng cung cấp:
• Ngân hàng có Open Banking API (Techcombank, MB, VPBank...): có thể lấy số dư realtime
• Ngân hàng không có API (một số ngân hàng quốc doanh): chỉ có thể nhập thủ công hoặc import file sao kê
• Cần liệt kê danh sách ngân hàng SCG VN đang sử dụng → đánh giá từng ngân hàng có API không
• Thiết kế hybrid: ngân hàng có API → kết nối tự động; ngân hàng không có API → upload file sao kê thủ công
• UI cần hiển thị rõ: ""Cập nhật lúc: HH DD/MM"" và nguồn dữ liệu (API / Nhập tay) để user biết độ tin cậy của số liệu" "Sếp muốn biết nguồn tiền ở từng ngân hàng realtime còn bao nhiêu, tiền gửi tiết kiệm... để sếp có quyết định điều chuyển tiền cho phù hợp.
Hệ thống có chức năng làm Memo để sếp duyệt việc mở tài khoản tiết kiệm (có form mẫu).
Chỗ tiền gửi tiết kiệm có Policy → hệ thống show thông tin thực tế có trong quy định của Policy."
M6.06 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Liên kết email nhận biết tiền vào/ra "Tự động nhận diện và ghi nhận giao dịch ngân hàng từ email thông báo:
• Màn hình quản lý dòng tiền vào/ra qua email ngân hàng: số tiền, nội dung, từ email nào, mail subject, liên kết với record ID trong BeON
• AI phân tích nội dung email (thường lộn xộn không cố định format) → extract thông tin chính xác
• Bổ sung trạng thái phê duyệt từng record để xác nhận số liệu đúng trước khi đưa qua MISA
• Lưu lịch sử thay đổi thông tin record (lognote)" NEW AI cần được train/prompt để xử lý đa dạng format email của các ngân hàng khác nhau (Vietcombank, BIDV, Techcombank...). Cần thu thập mẫu email thực tế từ SCG VN.
M6.07 M6 Quản lý Thu - Chi Cash In / Cash Out Quản lý Thu/Chi Tích hợp MISA "Đồng bộ dữ liệu thu/chi giữa BeON và MISA:
• Sync master data (danh mục KH, NCC, tài khoản kế toán)
• Ghi nhận thông tin giao dịch
• Đẩy dữ liệu từ BeON sang MISA
• Nhận sync-back dữ liệu từ MISA về BeON
• Xuất hóa đơn điện tử qua MISA" NEW Cần nghiên cứu MISA API documentation đầy đủ, đặc biệt cho phần sync master data và sync-back.
M7.01 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Liên kết dữ liệu làm PR Dữ liệu bảng kê traveling booking trên Xperise "Thông tin các DV booking trên Xperise trong kỳ -> link qua BeON để admin làm PR thanh toán cho Xperise
(xem API giá thế nào hoặc kiếm solution đơn giản hơn, hoặc data đưa vô 1 table trug gian ….)" NEW Cần xác định cấu trúc file Excel UTS gửi để thiết kế mapping chính xác.
M7.02 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Liên kết dữ liệu làm PR Link Data Salary để HR làm phiếu chi lương Hệ thống có thể link data salary tổng (trên BeON HR) qua PR để chi và hạch toán chi lương, BHXH (HR làm PR)
M7.03 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Liên kết dữ liệu làm PR Taxi_BeON Hệ thống có thể link thông tin bên function Taxi Info để láy dữ liệu làm PR
M7.04 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Liên kết dữ liệu làm PR Search chứng từ trên Thinkspace, e-contract
M7.05 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Liên kết dữ liệu làm PR Các hệ thống tương lai Như e-timesheet
M7.06 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Xuất file Excel Xuất theo định dạng Ts24 "Xuất dữ liệu từ BeON ra file Excel theo đúng định dạng chuẩn của hệ thống Tax24 để user import lên hệ thống thuế:
• Xác định số lượng template cần xuất
• Thiết kế mapping dữ liệu từ BeON vào từng ô của template Tax24" NEW Cần lấy file template Tax24 từ SCG VN để thiết kế mapping data.
M7.07 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Xuất file Excel Xuất theo định dạng JustForm "Xuất dữ liệu từ BeON ra file Excel theo đúng định dạng chuẩn của JustForm24:
• Xác định số lượng template cần xuất
• Thiết kế mapping dữ liệu từ BeON vào từng ô của template JustForm24" NEW Cần lấy file template JustForm24 từ SCG VN để thiết kế mapping data.
M7.08 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Cấu hình Master Data Cấu hình danh mục dùng chung "Quản lý các danh mục dùng chung toàn hệ thống: danh mục hàng hóa/dịch vụ, đơn vị tính, loại chi phí, loại hợp đồng...
Chức năng này đã có sẵn trong hệ thống BeON, chỉ cần cấu hình theo dữ liệu thực tế của SCG VN." PACKAGE Cần thu thập danh mục thực tế từ SCG VN để nhập dữ liệu ban đầu (data migration).
M7.09 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Cấu hình Master Data Cấu hình Cost Center / Department / Chart of Accounts "Quản lý cấu trúc tổ chức và sơ đồ tài khoản kế toán: Department, Team, Cost Center, Chart of Accounts, cost element
Chức năng này đã có sẵn trong hệ thống BeON." PACKAGE Cần lấy Chart of Accounts và cơ cấu tổ chức từ SCG VN (thường có sẵn trên MISA).
M7.10 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Cấu hình Master Data Cấu hình DOA / Policy / Approval Matrix "Cấu hình ma trận phê duyệt (DOA) và các policy nghiệp vụ:
• Approval Matrix: vai trò, ngưỡng tiền, loại giao dịch
• Policy config: ngưỡng hóa đơn, danh sách lý do pass thủ tục, hạn mức ngày công nợ...
Chức năng này đã có sẵn trong hệ thống BeON, cần cấu hình theo DOA thực tế của SCG VN." PACKAGE Đây là bước config quan trọng nhất trước khi go-live. Cần có file DOA chính thức từ SCG VN.
M7.11 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Reports & Dashboard Dashboard quản trị "Dashboard tổng hợp cho ban lãnh đạo:
• Dòng tiền dự kiến phải chi tuần này / tháng này
• Top 5 phòng ban tiêu nhiều tiền nhất
• Tình hình sử dụng ngân sách (% còn lại)
• Thiết kế theo hướng: BeON expose data thô chất lượng cao → Thinkspace (AI chatbot đã có sẵn và đang vận hành trong hệ thống KH) đọc data và tạo report/dashboard động theo yêu cầu từng người dùng" NEW "Thay đổi hướng thiết kế theo feedback KH: không build dashboard cứng, chỉ cần đảm bảo data API/export đủ tốt để Thinkspace AI tự tạo report.
Thinkspace là AI chatbot đã có sẵn và đang vận hành trong hệ thống của KH (SCG VN). Nhiệm vụ của BeON là expose data thô đủ tốt để Thinkspace đọc được — không cần build thêm dashboard cứng.
Cần xác định: (1) format/API mà Thinkspace dùng để đọc data từ BeON, (2) danh sách data fields Thinkspace cần access."
M7.12 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Reports & Dashboard Đối chiếu số liệu BeON vs MISA "Hệ thống tự động chạy đối chiếu cuối ngày / cuối tháng:
• So sánh: Tổng tiền đã duyệt chi trên BeON vs Tổng tiền thực tế đã chuyển trên MISA
• Kết quả khớp: hiển thị trạng thái ""OK"" (màu xanh)
• Kết quả lệch: cảnh báo đỏ, liệt kê chi tiết các giao dịch bị lệch (VD: BeON ghi đã chi nhưng MISA chưa thấy tiền đi) để KT kiểm tra
• Dữ liệu đối chiếu cũng có thể đưa vào Thinkspace để phân tích sâu hơn
-> Hỏi lại BAP cho rõ" NEW "Cần xác định tần suất chạy đối chiếu (real-time, cuối ngày, cuối tháng) và ai là người nhận cảnh báo khi lệch.
Kết quả đối chiếu nên được expose qua API để Thinkspace có thể đọc và tạo báo cáo reconciliation theo yêu cầu."
M7.13 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others "Action Dashboard
(Trung tâm Hành động & Nhắc nhở)" Nhắc tạm ứng quá hạn "Phần nhắc nhở tạm ứng được tích hợp vào màn hình Action Dashboard đã có sẵn trong hệ thống BeON — không xây dựng thành module riêng mà bổ sung thêm một mục/tab trong màn hình này.

Cách hiển thị trên Action Dashboard:
• Thêm mục ""Tạm ứng chưa hoàn"" vào danh sách action items
• Mỗi item hiển thị: tên NV, số tiền advance, ngày cam kết settle, số ngày đã trễ
• Màu sắc theo mức độ: vàng (< 7 ngày), cam (7–14 ngày), đỏ (> 14 ngày)
• Click vào item → navigate thẳng đến record PR Advance tương ứng

Logic nhắc nhở nền (background job — chạy hàng ngày):
• Quét tất cả PR Advance chưa Settled, so với ngày cam kết
• Trễ ≤ 7 ngày: gửi in-app notification cho NV
• Trễ > 7 ngày: thêm vào Action Dashboard của Team Lead
• Trễ > 14 ngày: thêm vào Action Dashboard của DGD
• Trễ > 30 ngày: thêm vào Action Dashboard của GD + highlight đỏ
• NV nhận thông báo → vào hệ thống → giải trình + cam kết ngày settle mới" NEW Tích hợp vào Action Dashboard đã có sẵn trong hệ thống BeON.
M7.14 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others "Action Dashboard
(Trung tâm Hành động & Nhắc nhở)" Nhắc tất toán thẻ tín dụng "Tích hợp vào Action Dashboard — thêm mục ""Thẻ tín dụng chưa tất toán"".

Cách hiển thị trên Action Dashboard:
• Mục ""Thẻ tín dụng chưa tất toán"": hiển thị danh sách NV có thẻ chưa tất toán theo chu kỳ
• Mỗi item: tên NV, số thẻ (ẩn bớt), số tiền chưa tất toán, ngày sao kê, số ngày còn lại
• Cảnh báo khi gần đến ngày sao kê (X ngày — configurable)

Logic nhắc nhở nền:
• Trước ngày sao kê X ngày → gửi in-app notification nhắc NV chủ thẻ
• Đến ngày sao kê chưa tất toán → item xuất hiện trên Action Dashboard của Team Lead
• Quá hạn tất toán → leo thang tương tự logic advance" NEW Tích hợp vào Action Dashboard
M7.15 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others "Action Dashboard
(Trung tâm Hành động & Nhắc nhở)" Resend nhắc duyệt PR / PV "Tích hợp vào Action Dashboard — thêm mục ""Đang chờ duyệt lâu"".

Cách hiển thị trên Action Dashboard:
• Với người tạo đơn: mục ""Đơn của tôi chờ duyệt lâu"" — liệt kê các PR/PV/Certificate đã gửi duyệt quá X ngày chưa có action
• Nút ""Gửi nhắc lại"" ngay trên từng item — bấm 1 click, không cần vào chi tiết
• Hiển thị: đã gửi nhắc X lần, lần cuối nhắc lúc HH DD/MM

Với người duyệt (Action Dashboard của approver):
• Các đơn chờ duyệt lâu được highlight/pin lên đầu danh sách
• Badge ""Đã nhắc X lần"" để approver biết người tạo đang chờ

Logic:
• Sau X ngày (configurable) chưa có action → hệ thống tự động gửi nhắc 1 lần/ngày
• Người tạo chủ động Resend: tối đa Y lần/ngày (configurable)" NEW
M7.16 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others "Action Dashboard
(Trung tâm Hành động & Nhắc nhở)" Nhắc xuất hóa đơn cho KH "Tích hợp vào Action Dashboard — thêm mục ""Hóa đơn cần xuất hôm nay / tuần này"".

Cách hiển thị:
• Danh sách KH đến ngày xuất HĐ theo kế hoạch (từ sub-function 4.3)
• Mỗi item: tên KH, số HĐ dự kiến, số tiền, ngày xuất theo kế hoạch
• Màu vàng: còn X ngày; màu đỏ: đã đến ngày / quá hạn
• Click → navigate đến màn hình xuất HĐ của KH đó" NEW
M7.17 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others "Action Dashboard
(Trung tâm Hành động & Nhắc nhở)" Nhắc công nợ KH quá hạn "Tích hợp vào Action Dashboard — thêm mục ""Công nợ KH quá hạn"".

Cách hiển thị:
• Danh sách KH có công nợ vượt quá số ngày quy định (mặc định 30 ngày)
• Mỗi item: tên KH, số tiền nợ, số ngày đã quá hạn, lần liên hệ gần nhất, lý do trễ (nếu đã cập nhật)
• Màu theo mức độ: vàng (30–45 ngày), cam (45–60 ngày), đỏ (>60 ngày)
• KT click vào item → cập nhật ghi chú liên hệ KH ngay trên màn hình
• Leo thang: quá hạn nghiêm trọng → item xuất hiện thêm trên Action Dashboard của KT trưởng / CFO" NEW
M7.18 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Tích hợp AI - ThinkSpace AI hỗ trợ trong việc tìm kiếm thông tin nhanh "Tìm trong document đã upload.
Kế toán lưu trự Dữ liệu link qua Thinkspace (cài đặt tự động lưu): PV, các dự liệu kèm theo,... (Thinkspace là đích đến)" CUSTOM
M7.19 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Tích hợp AI - ThinkSpace AI generate report theo yêu cầu Hỗ trợ tạo file report nhanh chóng hoặc trích xuất thông tin report nhanh chóng bắng AI CUSTOM
M7.20 M7 Liên kết Dữ liệu & Chức năng khác Data Integration & Others Tích hợp AI - ThinkSpace AI hỗ trợ trong việc hỏi đáp nhanh quy trình Bổ sung các kiến thức về quy trình của hệ thống Payment, hỗ trợ nhân viên hỏi đáp CUSTOM

	Lưu ý: Trong trường hợp các Công ty khác của SCG họ ko dùng full chức năng, nhưng chỉ dùng 1 phần thì có thể tách từng phần share cho các công ty dùng theo nhu cầu của  họ.															
	Ví dụ: Có công ty họ chỉ dùng phần E-signer, thì chỉ mở phần E-signer cho họ dùng (họ có thể API phần E-signer này với danh sách lao động trên hệ thống bên họ để dùng)															
	Hoặc họ chỉ dùng chức năng "Xin duyệt trước khi thực hiện hoạt động" trong Mục Advance thì cũng có thể tách ra cho họ dùng phần này thôi															

Đóng
