from datetime import time

from app.payment_manager import PaymentManager


def test_calculate_compensation():
    assert PaymentManager.calculate_compensation("MO", (time(9, 0), time(12, 0))) == 45
    assert PaymentManager.calculate_compensation("TH", (time(1, 0), time(3, 0))) == 50
    assert PaymentManager.calculate_compensation("SA", (time(14, 0), time(18, 0))) == 80
    assert PaymentManager.calculate_compensation("SU", (time(20, 0), time(21, 0)))
