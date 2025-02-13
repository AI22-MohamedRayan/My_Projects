const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

function isValidGmail(email) {
    const gmailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
    return gmailRegex.test(email);
}

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'nextstepmentor24@gmail.com',
        pass: 'igud dkzn eaua iyue' 
    }
});

app.post('/submit-form', (req, res) => {
    const { name, email, subject, message } = req.body;
    if (!name || !email || !subject || !message) {
        return res.status(400).json({ error: 'All fields are required' });
    }
    if (!isValidGmail(email)) {
        return res.status(400).json({ error: 'Please provide a valid Gmail address' });
    }
    const mailOptions = {
        from: email,
        to: 'nextstepmentor24@gmail.com',
        subject: subject,
        text: `
Name: ${name}
Email: ${email}
Subject: ${subject}
Message: ${message}
        `
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending email:', error);
            return res.status(500).json({ error: 'Failed to send email' });
        }
        console.log('Email sent:', info.response);
        res.status(200).json({ message: 'Form submitted successfully' });
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});