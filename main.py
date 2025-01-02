import asyncio
import edge_tts

# Hàm tạo giọng nói
async def text_to_speech(text, voice_name, output_file):
    try:
        communicator = edge_tts.Communicate(text, voice_name)
        await communicator.save(output_file)
        print(f"Đã lưu giọng nói vào file {output_file}")
    except edge_tts.exceptions.NoAudioReceived:
        print(f"Lỗi: Không nhận được âm thanh. Kiểm tra lại các tham số.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Danh sách các giọng nói có sẵn (Ví dụ cho tiếng Việt)
voices = {
    "nu": "vi-VN-HoaiMyNeural",  # Giọng nữ
    "nam": "vi-VN-NamMinhNeural",  # Giọng nam
}

# Văn bản muốn chuyển thành giọng nói
text = """
Mục tiêu
“Nếu không có mục tiêu thì chúng ta sẽ chẳng biết phải đi về đâu cả!”
“Lý do cuối cùng để thiết lập mục tiêu là để thúc đẩy bạn trở thành con người cần thiết để đạt được chúng.”
“Hãy lập ra các mục tiêu rồi sau đó hành động dựa trên chúng. Viết các ý tưởng ra giấy – cũng giống như xây nhà, bạn cần hoàn thiện bản vẽ trên giấy trước”
“Khi bạn biết mình muốn gì và muốn nó đủ mạnh mẽ, bạn sẽ tìm ra cách để đạt được nó.”
“Nếu bạn làm việc theo mục tiêu của mình, mục tiêu của bạn sẽ thực hiện theo bạn. Nếu bạn thực hiện theo kế hoạch của mình, kế hoạch của bạn sẽ thực hiện theo đúng kế hoạch của bạn. Bất cứ điều gì tốt đẹp chúng ta xây dựng đều cuối cùng xây dựng nên chúng ta
“Thành công là sự tiến bộ ổn định đối với các mục tiêu cá nhân của một người.”
“Mục tiêu tốt của lãnh đạo là giúp những người đang làm kém làm tốt và giúp những người đang làm tốt làm tốt hơn nữa.”
“Tất cả chúng ta đều cần nhiều mục tiêu tầm xa mạnh mẽ để giúp chúng ta vượt qua những trở ngại ngắn hạn.”
“Lý do chính để đặt mục tiêu là vì bạn phải hoàn thành mục tiêu đó là gì. Những gì nó tạo ra cho bạn sẽ luôn là giá trị lớn hơn nhiều so với những gì bạn nhận được. “
“Bạn không thể thay đổi điểm đến của mình trong một sớm một chiều, nhưng bạn có thể thay đổi hướng đi trong một sớm một chiều.”
“Nếu bạn không thiết kế kế hoạch cuộc sống của riêng bạn, rất có thể là bạn sẽ rơi vào kế hoạch của người khác. Và đoán những gì họ đã lên kế hoạch cho bạn?”
“Hạnh phúc không phải là thứ bạn trì hoãn cho tương lai; nó là thứ mà bạn thiết kế cho hiện tại. “
“Bắt đầu từ mọi lúc mọi nơi và với bất cứ thứ gì bạn có.”
 

Thời Gian
“Hãy dành thời gian thu thập quá khứ để có thể rút kinh nghiệm và đầu tư chúng cho tương lai.”
“Thời gian giá trị hơn tiền bạc. Bạn có thể nhận được nhiều tiền hơn, nhưng bạn không thể có được nhiều thời gian hơn.”
” Hãy tìm kiếm cơ hội, đừng bỏ lỡ cơ hội “.
”Nếu có hai hoặc ba người đồng thuận về một mục đích, không có gì là không thể”
“Thời gian giá trị hơn tiền bạc. Bạn có thể nhận được nhiều tiền hơn, nhưng bạn không thể có được nhiều thời gian hơn”.
“Không có cảm giác cấp bách, ham muốn mất đi giá trị của nó.”
“Hoặc bạn sử dụng thời gian, hoặc thời gian sử dụng bạn”
“Thời gian thật đắt đỏ. Khi bạn sử dụng một ngày, bạn có ít hơn một ngày để chi tiêu. Vì vậy, hãy đảm bảo rằng bạn chi tiêu từng khoản thời gian một cách khôn ngoan ”.
“Cuộc sống không chỉ là thời gian trôi qua. Cuộc sống là tập hợp của những trải nghiệm và cường độ của chúng ”.
“Bạn là trung bình của năm người mà bạn dành nhiều thời gian nhất.”
“Vấn đề của việc chờ đợi cho đến ngày mai là khi nó cuối cùng đến, nó được gọi là ngày hôm nay.”
 

Thay đổi bản thân (Be)
“Cuộc sống được tạo ra để bạn nhận những gì bạn xứng đáng chứ không phải những gì bạn muốn”
“Nếu bạn thay đổi, tất cả mọi thứ sẽ thay đổi cho phù hợp với bạn; đừng chờ đợi mọi thứ sẽ thay đổi cho bạn vì nó sẽ không thay đổi; thay đổi chính bản thân mình…. và mọi thứ sẽ thay đổi theo bạn”.
“Hãy nỗ lực cải thiện bản thân (BE) nhiều hơn nỗ lực làm (DO) công việc của mình, “giàu có” không phải là thứ bạn chạy theo, mà là thứ bạn hút về phía mình”
“Giá trị lớn trong cuộc sống không phải là những gì bạn nhận được (HAVE). Giá trị lớn trong cuộc sống là những gì bạn trở thành (BE)”.
“Bạn có thể có nhiều hơn những gì bạn có, bởi vì bạn có thể trở nên nhiều hơn những gì bạn đang là.”
“Nếu bạn làm việc chăm chỉ vì công việc của bạn, bạn sẽ chỉ đủ tiền để sống; Nhưng nếu bạn làm việc chăm chỉ cho chính bản thân bạn, bạn sẽ có một gia tài”.
“Làm việc chăm chỉ hơn cho bản thân bạn làm việc của bạn.”
“Nếu bản thân bạn không có giá trị… bạn sẽ không kiếm được nhiều tiền, trở thành con người có giá trị là chìa khóa để thành công”.
“Mức độ thành công của bạn sẽ hiếm khi vượt quá mức độ phát triển cá nhân của bạn.”
“Để hấp dẫn những mẫu người hấp dẫn, bạn phải là một người hấp dẫn. Để hấp dẫn những người có sức mạnh, bạn phải là một người có sức mạnh. Để hấp dẫn những người trung thành, bạn phải là một người trung thành. Thay vì tìm kiếm những người như thế, hãy thay đổi chính bản thân mình và rồi bạn sẽ hấp dẫn họ”.
“Đừng ước rằng mọi chuyện sẽ dể dàng hơn; Hãy ước bạn tài giỏi hơn.
Đừng ước rằng bạn sẽ có ít rắc rối trong cuộc sống; Hãy ước bạn có nhiều kỹ năng hơn.
Đừng ước cuộc sống của bạn có ít thử thách; Hãy ước bạn khôn ngoan hơn.”
“Tính cách là một phẩm chất thể hiện nhiều đặc điểm quan trọng, chẳng hạn như tính chính trực, lòng dũng cảm, tính kiên trì, sự tự tin và trí tuệ. Không giống như dấu vân tay của bạn mà bạn sinh ra và không thể thay đổi, tính cách là thứ mà bạn tạo ra bên trong chính mình và phải chịu trách nhiệm thay đổi ”.
“Thách thức lớn là trở thành tất cả những gì bạn có khả năng trở thành. Bạn không thể tin những gì nó làm đối với tinh thần con người để tối đa hóa tiềm năng con người của bạn và vươn mình đến giới hạn. ”
“Những bức tường mà bạn dựng lên xung quanh mình có thể giúp bạn tránh được sự đau khổ, những chúng cũng ngăn bạn có những niềm vui.”
“Bạn phải chịu trách nhiệm cá nhân. Bạn không thể thay đổi hoàn cảnh, mùa, hay gió, nhưng bạn có thể thay đổi chính mình. Đó là điều mà bạn có trách nhiệm. ”
“Học cách hạnh phúc với những gì bạn có trong khi theo đuổi tất cả những gì bạn muốn”.
“Bất cứ điều gì tốt đẹp chúng ta xây dựng đều cuối cùng xây dựng chúng ta.”
“Thách thức của lãnh đạo là phải mạnh mẽ, nhưng không thô lỗ; tử tế, nhưng không yếu đuối; hãy mạnh dạn, nhưng không phải là một kẻ bắt nạt; chu đáo, nhưng không lười biếng; khiêm tốn, nhưng không rụt rè; hãy tự hào, nhưng không kiêu ngạo; có sự hài hước, nhưng không có sự điên rồ. “
“Lợi nhuận thì tốt hơn tiền lương, vì tiền lương giúp bạn trang trải cuộc sống bình thường còn lợi nhuận sẽ tạo ra cho bạn sự giàu có”.
Lợi nhuận = Giá trị x Thời gian x Quy mô
“Sau khi đã trở thành triệu phú, bạn có thể cho tất cả tiền của mình đi làm không thương tiếc bởi vì bây giờ tiền không quan trọng nữa, cái quan trọng là khối óc của bạn đã được rèn luyện trong quá trình trở thành triệu phú”.
“Bạn càng biết nhiều thì bạn càng ít phải nói”.
 

Học tập
“Cuộc sống của bạn có đi lên hay không, tất cả nằm ở NHỮNG CUỐN SÁCH BẠN ĐỌC VÀ NHỮNG NGƯỜI BẠN GẶP”.
“Nếu bạn phải bỏ lỡ một bữa ăn, nhưng đừng bỏ lỡ một cuốn sách.”
“Cuốn sách bạn chưa đọc sẽ không giúp ích gì.”
” Hãy coi quá khứ là trường học và bước tới tương lai với sự háo hức”.
“Giáo dục chính quy sẽ giúp bạn kiếm sống; tự giáo dục bản thân sẽ làm nên tài sản cho bạn ”.
“Đọc sách là điều cần thiết cho những ai muốn vượt lên trên tầm thường.”
“Học tập là sự khởi đầu của sự giàu có. Học tập là sự khởi đầu của sức khỏe. Học tập là sự khởi đầu của tâm linh. Tìm kiếm và học hỏi là nơi mà quá trình tất cả điều kỳ diệu bắt đầu”
“Đừng chỉ đọc những thứ DỄ DÀNG. Bạn có thể được GIẢI TRÍ, nhưng bạn sẽ không bao giờ PHÁT TRIỂN.”
” Chúng ta bị ảnh hưởng bởi những gì chúng ta học, bởi những gì chúng ta biết và bởi những quyết định của chúng ta”.
“Lý do mà tiểu thuyết thú vị hơn bất kỳ hình thức văn học nào khác, đối với những người thực sự thích nghiên cứu con người, là trong tiểu thuyết, tác giả thực sự có thể nói sự thật mà không làm nhục bản thân.”
“Nếu ai đó đi nhầm đường, anh ta không cần động lực để tăng tốc. Điều anh ấy cần là giáo dục để xoay chuyển tình thế của anh ấy ”.
“Đầu tư vào bản thân, đầu tư vào việc tự giáo dục bản thân và sau đó lấy kiến thức đó và sử dụng nó để giúp người khác đạt được điều họ muốn và cần trong cuộc sống. Trong quá trình này, bạn sẽ có được quyền lực và tự do tài chính ”.
“Đừng bao giờ miễn cưỡng số tiền bạn bỏ ra cho việc học của mình.”
“Một cuốn tiểu thuyết không bao giờ là bất cứ thứ gì, mà là một triết lý được đưa vào hình ảnh.”
“Gặp gỡ những người có điều gì đó giá trị để chia sẻ với bạn. Tác động của chúng sẽ tiếp tục có ảnh hưởng đáng kể đến cuộc sống của bạn rất lâu sau khi chúng ra đi. “
 
Kỷ luật
“Kỷ luật là cầu nối giữa các mục tiêu và hoàn thành”
Bốn câu hỏi quan trọng trong cuộc đời bạn:
“Tại sao bạn cần phải cố gắng?”/ “Tại sao không?”
“Tại sao không phải là Bạn?”/ “Tại sao không phải bây giờ?”
“Tất cả chúng ta phải chịu một trong hai điều: nỗi đau của kỷ luật hoặc nỗi đau của sự hối tiếc hoặc thất vọng.”
“Nếu muốn thì bạn sẽ tìm cách. Nếu không muốn, bạn sẽ tìm lý do”
“Kỷ luật là nền tảng mà tất cả thành công được xây dựng. Thiếu kỷ luật chắc chắn sẽ dẫn đến sự thất bại”
“Đối với mọi nỗ lực có kỷ luật sẽ có nhiều phần thưởng.”
“Những lời khẳng định rất quan trọng. Nhưng khẳng định mà thiếu đi kỷ luật chính là sự bắt đầu của ảo tưởng.
“Động lực là thứ giúp bạn bắt đầu; thói quen là thứ giữ cho bạn đi tới.”
“Đừng nói,“ Nếu tôi có thể, tôi sẽ làm. Hãy nói, Nếu tôi có thể, tôi sẽ làm. ”
“Kỷ luật có trong nó tiềm năng tạo ra những điều kỳ diệu trong tương lai.”
 

Giao tiếp
“Lời nói làm được hai điều chính: Chúng cung cấp thức ăn cho trí óc và tạo ra ánh sáng cho sự hiểu biết và nhận thức.”
“Hỏi là bắt đầu nhận. Hãy chắc chắn rằng bạn không đi ra biển với một thìa cà phê. Ít nhất hãy lấy một cái xô để bọn trẻ không cười bạn. “
“Tính cách không phải là thứ bạn sinh ra và không thể thay đổi, giống như dấu vân tay của bạn. Đó là thứ mà bạn không sinh ra và phải chịu trách nhiệm hình thành ”.
“Giao tiếp hiệu quả là 20% những gì bạn biết và 80% cảm nhận của bạn về những gì bạn biết.”
“Hãy tận dụng mọi cơ hội để rèn luyện kỹ năng giao tiếp của mình để khi có dịp quan trọng, bạn sẽ có năng khiếu, tác phong, sự sắc sảo, trong sáng, và cảm xúc để ảnh hưởng đến người khác.”
“Đừng tham gia vào một đám đông dễ dãi; bạn sẽ không phát triển. Hãy đến nơi mà kỳ vọng và yêu cầu thực hiện cao. ”
“Bạn không thể thành công một mình. Thật khó để tìm thấy một ẩn sĩ giàu có. “
 

Hành động
“Nếu bạn tiến về phía tôi một bước, tôi sẽ tiến về phía bạn một bước – Kinh cựu ước.
Nếu bạn tiến về phía ước mơ một bước – ước mơ sẽ tiến về phía bạn một bước.”
“Để giải quyết bất kỳ vấn đề, đây là ba câu hỏi để tự hỏi mình: Thứ nhất, những gì tôi có thể làm là gì? Thứ hai, những gì tôi có thể đọc? Và thứ ba, tôi có thể hỏi ai?”
“Hãy chọn hành động, đừng chọn nghỉ ngơi. Chọn sự thật, đừng chọn ảo tưởng. Chọn một nụ cười, đừng chọn một cái nhíu mày. Chọn tình yêu, đừng chọn thù hận. Chọn những điều tốt đẹp trong mọi việc, và chọn thời cơ cũng như cơ hội để làm việc
“Để thành công trong kinh doanh, đơn giản là chỉ cần nói với thật nhiều người hàng ngày. Và điều phấn khởi nhất là có rất nhiều người để bạn nói!”
“Thảm họa kinh tế bắt đầu với một triết lý làm ít hơn và muốn nhiều hơn nữa”.
“Hãy học loài kiến, kiến không bao giờ từ bỏ. Kiến nghĩ tới mùa đông khi đang là mùa hè và luôn làm việc chăm chỉ. Hãy cẩn thận vào mùa hè và đừng dựng xây cái gì trên cát.”
“Chúng ta không nhận được gì từ thời gian, chúng ta nhận được những gì mà chúng ta đã LÀM trong thời gian đó”
“Điều tồi tệ nhất mà người ta có thể làm là không cố gắng, không nhận thức được điều mình muốn và không chịu thua nó, dành nhiều năm trong sự tổn thương thầm lặng tự hỏi liệu điều gì đó có thể thành hiện thực – không bao giờ biết được.”
“Thành công không kỳ diệu cũng không huyền bí. Thành công là kết quả tự nhiên của việc áp dụng một cách nhất quán các nguyên tắc cơ bản. ”
“Nếu không có hoạt động liên tục, các mối đe dọa của cuộc sống sẽ sớm lấn át các giá trị.”
“Thành công không gì khác hơn là một vài kỷ luật đơn giản, được thực hành mỗi ngày.”
“Hãy thực hiện theo tiến độ có thể đo lường được trong thời gian hợp lý.”
“Chính bộ cánh buồm, không phải hướng gió quyết định con đường mà chúng ta sẽ đi.”
“Bất cứ ai phục vụ nhiều người thì tự xếp mình vào hàng vĩ đại – giàu có, lợi nhuận lớn, hài lòng lớn, danh tiếng lớn và niềm vui lớn.”
“Nếu bạn không thích mọi thứ như thế nào, hãy thay đổi nó! Bạn không phải là một cái cây. “
“Những khó khăn bạn gặp sẽ tự giải quyết khi bạn thăng tiến. Hãy tiếp tục, và ánh sáng sẽ bình minh, và chiếu sáng với sự rõ ràng ngày càng tăng trên con đường của bạn. “
“Chỉ có 3 màu, 10 chữ số và 7 nốt nhạc; những gì chúng ta làm với chúng mới là điều quan trọng. ”
“Những NGƯỜI ÍT LÀM là sự ghen tị của nhiều NGƯỜI CHỈ XEM.”
“Lao động sinh ra ý tưởng”.
“Nếu bạn không sẵn sàng mạo hiểm điều bất thường, bạn sẽ phải giải quyết cho điều bình thường.”
“Nếu bạn không thay đổi cách bạn đang làm, bạn sẽ luôn có những gì bạn đang có.”
“Đừng mang nhu cầu của bạn ra thị trường, hãy mang kỹ năng của bạn. Nếu bạn cảm thấy không khỏe, hãy nói với bác sĩ của bạn, nhưng không nói với thị trường. Nếu bạn cần tiền, hãy đến ngân hàng, nhưng không phải đến chợ ”.
“Chúng ta được trả tiền để mang lại giá trị cho thị trường.”
Thái độ tích cực
“Lời khuyên là hãy chủ động, lựa chọn thái độ đúng đắn để đối mặt với cuộc đời”
“Nó quyết định xem ta có đọc hay không, cố gắng hay từ bỏ, tự trách mình hay đổ lỗi cho người khác khi gặp thất bại. Nó quyết định việc ta nói dối hay nói thật, chần chừ, bước tiếp hay rút lui. Thái độ là cái quyết định sự thành bại của bản thân chúng ta”
“Hãy coi quá khứ là trường học và bước tới tương lai với sự háo hức”
“Những lời bào chữa là cái đinh dùng để xây một ngôi nhà thất bại.”
” Nếu muốn thì bạn sẽ tìm cách. Nếu không muốn, bạn sẽ tìm lý do”.
“Thất bại chỉ đơn giản là một vài sai sót trong phán đoán, lặp đi lặp lại mỗi ngày.”
“Chăm sóc cơ thể của bạn. Đó là nơi duy nhất bạn phải sống”
“Hạnh phúc không phải là một cái gì đó bạn trì hoãn cho tương lai; nó là cái gì bạn thiết kế cho hiện tại”
“Chúng ta bị ảnh hưởng bởi những gì chúng ta học, bởi những gì chúng ta biết và bởi những quyết định của chúng ta”
“Trong cuộc đời có một số ít sự việc tạo nên 80% sự khác biệt. Hãy liên tục tìm kiếm sự việc tạo nên nhiều sự khác biệt nhất”
“Đây là lý do tại sao rất nhiều người không thành công. Họ chỉ chú tâm vào những việc vụn vặt. Họ dành quá nhiều thời gian vào những việc không mang lại hiệu quả”
“Hãy canh gác cánh cửa tâm trí. Việc chúng ta trở thành thế nào chủ yếu được quyết định bởi những người chúng ta gặp, những sự kiện chúng ta tham gia, những cuốn sách chúng ta đọc, và lối sống mà chúng ta lựa chọn”.
“Mạnh mẽ nhưng không khiếm nhã. Tốt bụng nhưng không yếu đuối. Dũng cảm nhưng không phải là kẻ bắt nạt. Khiêm tốn nhưng không nhút nhát. Nghĩ kĩ nhưng không lười biếng. Tự hào nhưng không tự mãn. Hài hước nhưng không điên rồ.”
“Tất cả chúng ta phải tiến hành một cuộc chiến dữ dội, suốt đời chống lại lực kéo đi xuống liên tục. Nếu chúng ta thư giãn, lũ bọ và cỏ dại của sự tiêu cực sẽ di chuyển vào khu vườn và lấy đi mọi thứ có giá trị ”.
“Bạn phải chịu trách nhiệm cá nhân. Bạn không thể thay đổi hoàn cảnh, các mùa, hoặc gió, nhưng bạn có thể thay đổi chính mình”
“Trưởng thành là khả năng gặt hái được mà không cần xin lỗi và không phàn nàn khi mọi thứ không suôn sẻ.”
“Hãy để người khác dẫn dắt cuộc sống nhỏ bé, nhưng không phải bạn. Hãy để người khác tranh luận những chuyện nhỏ nhặt, nhưng không phải bạn. Hãy để những người khác khóc vì những chuyện nhỏ nhặt, nhưng bạn thì không nên. Hãy để người khác để tương lai của họ vào tay người khác chứ không phải bạn ”.
“Triết lý của bạn quyết định liệu bạn sẽ tuân theo các kỷ luật hay tiếp tục mắc lỗi.”
“Thà nói nhỏ còn hơn nói quá. Hãy để mọi người ngạc nhiên rằng nó còn nhiều hơn những gì bạn đã hứa và dễ dàng hơn những gì bạn đã nói ”.
“Một số người trồng vào mùa xuân và để lại vào mùa hè. Nếu bạn đã đăng ký một phần, hãy xem phần đó. Bạn không cần phải ở lại mãi mãi, nhưng ít nhất hãy ở lại cho đến khi bạn nhìn thấy nó. “
“Một phần di sản của bạn trong xã hội này là cơ hội để trở nên độc lập về tài chính.”
“Tất cả chúng ta đều biết nhiều cách khác nhau để kiếm sống. Điều hấp dẫn hơn nữa là tìm ra cách để kiếm nhiều tiền. “
“Sự giàu có không phải là vấn đề của trí thông minh, nó là vấn đề của nguồn cảm hứng.”
 

Chia sẻ
“Cho đi tốt hơn nhận lại bởi vì cho đi bắt đầu quá trình nhận lại.”
” Lời nói của bạn tạo ra giấc mơ để ai đó có thể hiểu được nó, để ai đó có thể nhìn thấy nó, để ai đó có thể hành động. Đó chính là vai trò của bạn.”
Khi chia sẻ một ý tưởng với mười người thì họ sẽ được nghe nó một lần, nhưng bạn sẽ được nghe mười lần, có nghĩa là bạn được lợi nhiều nhất từ việc chia sẻ đó. Nếu điều gì đó có ý nghĩa với bạn, hãy tìm cách chia sẻ
“Ý tưởng tốt – là ý tưởng mà bạn dành thời gian để nghiền ngẫm. Ý tưởng là thứ rất vi tế. Chúng đang chờ những người nỗ lực tìm kiếm chúng, và trừ khi bạn nỗ lực tìm kiếm, còn không thì chúng mãi mãi ẩn mình”
“Ý tưởng có thể thay đổi cuộc đời. Đôi khi tất cả những gì bạn cần để mở cửa chỉ là thêm một ý tưởng hay ”.
“Để thành công trong kinh doanh, đơn giản là chỉ cần nói với thật nhiều người hàng ngày. Và điều phấn khởi nhất là có rất nhiều người để bạn nói!”
"""

# Tạo giọng nói nam
asyncio.run(text_to_speech(text, voices["nam"], "output_nam.mp3"))

# Tạo giọng nói nữ
asyncio.run(text_to_speech(text, voices["nu"], "output_nu.mp3"))
