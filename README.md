====โปรแกรมออมเงินสู่ความฝัน====
โปรแกรมเนื้อมีหน้าที่ คำนวรเงินที่จะต้องเก็บเพื่อเอาไปใช้ในสิ่งที่ผู้ใช้ชอบหรืออยากทำ

1.ที่มาและความสำคัญ (Introduction)
สร้างโปรเจกตืนี้มาเพื่อการออมเงินของตัวเอง้พื่อสิ่งที่อยากได้
ปัญหาที่พบ = การทำโปรแกรมของตัวเองที่ไม่ค่อยถนัด
เป้าหมาย = ต้องการให้โปรแกรมคำนวณรายละเอียดในส่วนของการเก็บเงินเพื่อที่จะเอาใว้ใช้ในสิ่งที่ผู้ใช้ต้องการ

2.ความสามารถของโปรแกรม (Features)
 2.1การคำนวณเงินที่ใช้ในเป้าหมาย
 2.2การบอกสัดส่วนเกี่ยวกับเงินว่าขาดเงินอีกหรือเงินครบตามเป้าหมายแล้ว

3.เครื่องมือที่ใช้ (Teach Stack)
 3.1เครื่องมือในการสร้างโค้ด = Colab , Visual StudioCode
 3.2เครื่องมือในการใช้หาข้อมูลหรือการช่วยทำ = Google , Chat GPT , Gemini

4.ตัวอย่างการใช้งาน (Screenshots)
<img width="542" height="865" alt="สกรีนช็อต 2026-02-19 220633" src="https://github.com/user-attachments/assets/6db5faef-b51d-4b0c-be09-23fd2de79abf" />

5.วิธีการใช้งาน (How to run)
[Uploading code_23.HTML…]()
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>โปรแกรมออมเงินสู่ความฝัน</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f6ff;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            background: #ffffff;
            padding: 20px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #2c3e50;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }
        button {
            margin-top: 15px;
            width: 100%;
            padding: 10px;
            background: #4a6cff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #3a56d4;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #eef2ff;
            border-radius: 8px;
        }
        .footer {
            text-align: center;
            margin-top: 15px;
            font-size: 14px;
            color: gray;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>💰 โปรแกรมออมเงินสู่ความฝัน</h2>

    <label>ชื่อผู้ใช้</label>
    <input type="text" id="username">

    <label>เก็บเงินเพื่ออะไร</label>
    <input type="text" id="goal">

    <label>ต้องการเก็บเงินทั้งหมด (บาท)</label>
    <input type="number" id="target">

    <label>จำนวนวันที่ออม</label>
    <input type="number" id="days">

    <label>ออมเงินวันละ (บาท)</label>
    <input type="number" id="daily">

    <button onclick="calculate()">คำนวณผลการออม</button>

    <div class="result" id="result"></div>

    <div class="footer">
        ผู้จัดทำโดยนายแทนทัย ฉิมวิเชียร ม.4/4 เลขที่ 23
    </div>
</div>

<script>
    function calculate() {
        let username = document.getElementById("username").value;
        let goal = document.getElementById("goal").value;
        let target = parseFloat(document.getElementById("target").value);
        let days = parseInt(document.getElementById("days").value);
        let daily = parseFloat(document.getElementById("daily").value);

        let total = days * daily;
        let resultText = `
            <h3>📊 สรุปผลการออม</h3>
            <p><b>ชื่อผู้ใช้:</b> ${username}</p>
            <p><b>เป้าหมาย:</b> ${goal}</p>
            <p><b>จำนวนวันที่ออม:</b> ${days} วัน</p>
            <p><b>เงินที่ออมได้ทั้งหมด:</b> ${total} บาท</p>
        `;

        if (total >= target) {
            let extra = total - target;
            resultText += `
                <p style="color:green;">🎉 ยินดีด้วย! คุณออมถึงเป้าหมายแล้ว</p>
                <p>💰 เงินที่เหลือ: ${extra} บาท</p>
            `;
        } else {
            let missing = target - total;
            resultText += `
                <p style="color:red;">❌ ยังออมไม่ถึงเป้าหมาย</p>
                <p>คุณขาดเงินอีก: ${missing} บาท</p>
            `;
        }

        document.getElementById("result").innerHTML = resultText;
    }
</script>

</body>
</html>
