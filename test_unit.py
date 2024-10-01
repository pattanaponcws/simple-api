import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()  # สร้าง test client
        self.app.testing = True  # ตั้งค่าให้เป็น testing mode

    def test_getcode(self):
        response = self.app.get("/getcode")  # ใช้ test client เพื่อเรียก endpoint
        self.assertEqual(response.data.decode(), "getcode")  # ตรวจสอบค่าที่ส่งกลับ
        
    def test_plus(self):
        response = self.app.get("/plus/5/6")
        self.assertEqual(response.data.decode(), "5 + 6 = 11")

        response = self.app.get("/plus/1/4")
        self.assertEqual(response.data.decode(), "1 + 4 = 5")

        response = self.app.get("/plus/103/56")
        self.assertEqual(response.data.decode(), "103 + 56 = 159")

        # Test for invalid input
        response = self.app.get("/plus/a/4")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})

    def test_is_prime_17 (self):
        response = self.app.get("/is_prime/17")
        self.assertEqual(response.data.decode(), "true")

    def test_is_prime_36 (self):
        response = self.app.get("/is_prime/36")
        self.assertEqual(response.data.decode(), "false")

    def test_is_prime_18219 (self):
        response = self.app.get("/is_prime/13219")
        self.assertEqual(response.data.decode(), "true")