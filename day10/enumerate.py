from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


class Coffee(Product):
    def __init__(self, name, price, caffeine_content):
        super().__init__(name, price)
        self.caffeine_content = caffeine_content

    def display_info(self):
        print(f"{self.name} - {self.price}원, 카페인 함량: {self.caffeine_content}mg")


class Beverage(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def display_info(self):
        print(f"{self.name} - {self.price}원, 카페인이 포함되어 있지 않습니다.")


class Inventory:
    def __init__(self):
        self.items = {}

    def add_product(self, product):
        self.items[product.get_name()] = product
        product.display_info()

    def update_product_price(self, name, new_price):
        if name in self.items:
            self.items[name].set_price(new_price)
            print(f"{name}의 가격이 {new_price}원으로 변경되었습니다.")
        else:
            print("메뉴에 해당 제품이 존재하지 않습니다.")

    def delete_product(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} 메뉴에서 삭제되었습니다.")
        else:
            print("메뉴에 해당 제품이 존재하지 않습니다.")

    def get_inventory(self):
        return self.items


from datetime import datetime


class SalesRecord:
    def __init__(self, product, quantity, total_price):
        self.product = product
        self.quantity = quantity
        self.total_price = total_price
        self.timestamp = datetime.now()  # 현재 시간을 timestamp로 저장

    def display_sales_info(self):
        print(
            f"제품: {self.product.get_name()}, 수량: {self.quantity}, 총액: {self.total_price}원, 판매시간: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")


class SalesHistory:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def display_all_sales(self):
        if not self.records:
            print("판매 기록이 없습니다.")
        for record in self.records:
            record.display_sales_info()

    def find_sales_by_date(self, date):
        # date는 'YYYY-MM-DD' 형식의 문자열로 가정
        found_records = [record for record in self.records if record.timestamp.strftime('%Y-%m-%d') == date]
        if not found_records:
            print(f"{date}에 해당하는 판매 기록이 없습니다.")
        else:
            for record in found_records:
                record.display_sales_info()


class Application:
    def __init__(self):
        self.inventory = Inventory()
        self.sales_history = SalesHistory()  # 판매 기록을 저장할 리스트

    def run(self):
        while True:
            print("1. 커피 판매")
            print("2. 커피 메뉴 추가")
            print("3. 커피 메뉴 수정")
            print("4. 커피 메뉴 삭제")
            print("5. 판매 기록 보기")
            print("6. 프로그램 종료")
            action = input("원하는 작업 번호를 입력하세요: ")

            if action == "1":
                self.handle_sale()
            elif action == "2":
                self.handle_add_menu()
            elif action == "3":
                self.handle_update_menu()
            elif action == "4":
                self.handle_delete_menu()
            elif action == "5":
                self.handle_view_sales()
            elif action == "6":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")
    def handle_sale(self):
        inventory_items = self.inventory.get_inventory()
        if not inventory_items:
            print("판매할 제품이 없습니다.")
            return

        print("판매할 제품을 선택하세요:")
        for index, (name, product) in enumerate(inventory_items.items(), start=1):
            product.display_info()

        choice = int(input("번호를 입력하세요: ")) - 1
        product_names = list(inventory_items.keys())
        if 0 <= choice < len(product_names):
            product = inventory_items[product_names[choice]]
            quantity = int(input(f"판매할 {product.get_name()}의 수량을 입력하세요: "))
            total_price = quantity * product.get_price()
            # SalesRecord 인스턴스 생성 및 기록
            new_sale = SalesRecord(product, quantity, total_price)
            self.sales_history.add_record(new_sale)
            new_sale.display_sales_info()
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

    def handle_add_menu(self):
        product_type = input("제품 유형을 입력하세요 (커피, 비카페인): ")
        name = input("제품 이름을 입력하세요: ")
        price = int(input("제품 가격을 입력하세요: "))
        if product_type.lower() == "커피":
            caffeine = int(input("카페인 함량(mg)을 입력하세요: "))
            self.inventory.add_product(Coffee(name, price, caffeine))
        elif product_type.lower() == "비카페인":
            self.inventory.add_product(Beverage(name, price))
        else:
            print("잘못된 제품 유형입니다. 다시 시도해주세요.")

    def handle_update_menu(self):
        name = input("가격을 변경할 제품 이름을 입력하세요: ")
        new_price = int(input("새로운 가격을 입력하세요: "))
        self.inventory.update_product_price(name, new_price)

    def handle_delete_menu(self):
        name = input("삭제할 제품 이름을 입력하세요: ")
        self.inventory.delete_product(name)

    def handle_view_sales(self):
        print("전체 판매 기록 보기")
        self.sales_history.display_all_sales()

app = Application()
app.run()
