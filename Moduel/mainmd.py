# นำเข้า (Import) ทั้ง 10 โมดูล
import logger
import config
import validator
import calculator
import formatter
import database
import discount
import inventory
import user
import notification

def run_app():
    print("=" * 40)
    # 1. เรียกใช้ config
    print(f"กำลังเริ่มทำงาน: {config.get_app_info()}")
    
    # 2. เรียกใช้ logger
    logger.log("เริ่มต้นกระบวนการซื้อสินค้า...")

    # ข้อมูลสินค้าทดสอบ
    product_name = "Laptop"
    price = 25000.0
    quantity = 2
    current_stock = 5
    user_name = "JohnDoe"

    # 3. เรียกใช้ validator
    if not validator.is_positive_number(price):
        print("ราคาไม่ถูกต้อง")
        return

    # 4. เรียกใช้ inventory
    if inventory.check_stock(current_stock, quantity):
        logger.log(f"สินค้า {product_name} มีเพียงพอในสต็อก")
    else:
        print("สินค้าไม่พอ")
        return

    # 5. เรียกใช้ calculator
    raw_total = calculator.calculate_total(price, quantity)

    # 6. เรียกใช้ discount
    final_price = discount.apply_discount(raw_total, discount_percent=10) # ลด 10%

    # 7. เรียกใช้ user
    user_info = user.get_user_profile(user_name)

    # 8. เรียกใช้ formatter
    formatted_price = formatter.format_currency(final_price)
    print(f"ลูกค้า: {user_info['username']} | ยอดชำระหลังหักส่วนลด: {formatted_price}")

    # 9. เรียกใช้ database
    database.save_data("last_order", {"user": user_name, "total": final_price})
    logger.log("บันทึกข้อมูลการสั่งซื้อลง Database สำเร็จ")

    # 10. เรียกใช้ notification
    msg = notification.send_receipt(user_info['username'], formatted_price)
    print(f"[NOTIFICATION]: {msg}")
    
    print("=" * 40)

if __name__ == "__main__":
    run_app()