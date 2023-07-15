from reportlab.pdfgen import canvas

c = canvas.Canvas("output_file/hello.pdf", pagesize=(500, 500))  # Cというオブジェクト
c.setFont("Courier", 50)
c.drawString(50, 200, "Hello World")  # (x, y)mmではなくpoint 用紙の左下が起点
c.showPage()
c.drawString(50, 200, "Hello World")
c.showPage()  # ページに出力
c.save()  # 保存
