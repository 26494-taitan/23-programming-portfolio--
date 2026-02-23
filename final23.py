"""

เลือกโจทย์ : โปรแกรมคำนวณอายุจากปีเกิด
I : ปีเกิด (พ.ศ)
P : นำ ปีปัจจุบัน - ปีเกิด
O : แสดงอายุ
ตัวแปร : birth-year , current_year , age

"""
ทำ .HTML ใน vscode
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>โปรแกรมคำนวณอายุ</title>

<style>
    body {
        margin: 0;
        font-family: "Sarabun", sans-serif;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    .card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        width: 380px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        animation: fadeIn 1s ease-in-out;
    }

    h1 {
        margin-bottom: 10px;
    }

    input {
        width: 80%;
        padding: 12px;
        border-radius: 10px;
        border: none;
        margin: 15px 0;
        font-size: 16px;
        text-align: center;
    }

    button {
        padding: 12px 25px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        background: linear-gradient(45deg, #ff6ec4, #7873f5);
        color: white;
        transition: 0.3s;
    }

    button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

    #result {
        margin-top: 20px;
        font-size: 20px;
        font-weight: bold;
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
    }

    .credit {
        margin-top: 20px;
        font-size: 13px;
        opacity: 0.8;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
</style>
</head>

<body>

<div class="card">
    <h1>🎂 โปรแกรมคำนวณอายุ</h1>
    <p>กรุณากรอกปีเกิด (พ.ศ.)</p>

    <input type="number" id="birthYear" placeholder="เช่น 2550">

    <br>
    <button onclick="calculateAge()">คำนวณอายุ</button>

    <div id="result"></div>

    <div class="credit">
        ทำโดย นายแทนทัย ฉิมวิเชียร ม.4/4 เลขที่ 23
    </div>
</div>

<script>
function calculateAge() {
    let birthYear = document.getElementById("birthYear").value;
    let currentYear = new Date().getFullYear() + 543; // แปลง ค.ศ. เป็น พ.ศ.

    if (birthYear === "" || birthYear <= 0) {
        document.getElementById("result").innerHTML = "⚠ กรุณากรอกปีเกิดให้ถูกต้อง";
        document.getElementById("result").style.opacity = "1";
        return;
    }

    let age = currentYear - birthYear;

    let resultText = "🎉 คุณมีอายุประมาณ " + age + " ปี";
    let resultDiv = document.getElementById("result");
    resultDiv.innerHTML = resultText;
    resultDiv.style.opacity = "1";
}
</script>

</body>
</html>
