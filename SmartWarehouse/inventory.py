from database.db import get_connection


def add_product(product_code, product_name, quantity, location):
    conn = get_connection()

    conn.execute(
        """
        INSERT OR REPLACE INTO inventory
        (product_code, product_name, quantity, location)
        VALUES (?, ?, ?, ?)
        """,
        (product_code, product_name, quantity, location)
    )

    conn.commit()
    conn.close()


def update_quantity(product_code, quantity):
    conn = get_connection()

    conn.execute(
        """
        UPDATE inventory
        SET quantity = ?
        WHERE product_code = ?
        """,
        (quantity, product_code)
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    add_product("P001", "ตัวอย่างสินค้า", 100, "A-01")
    print("เพิ่มสินค้า P001 สำเร็จ")
