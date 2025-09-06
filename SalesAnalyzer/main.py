import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import datetime

class SalesAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.sales_data = []
        self.monthly_sales = defaultdict(float)

    def read_sales_data(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
                amount = float(row['amount'])
                self.sales_data.append({'date': date, 'product': row['product'], 'amount': amount})
                self.monthly_sales[date.strftime('%Y-%m')] += amount
    def generate_sales_graph(self):
        months = list(self.monthly_sales.keys())
        sales = list(self.monthly_sales.values())

        plt.figure(figsize=(10,6))
        plt.plot(months, sales, marker='o', color='b')
        plt.title("Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Sales Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("monthly_sales.png")
        plt.show()

    def calculate_average_sale(self):
        return sum(self.monthly_sales.values()) / len(self.monthly_sales)

    def get_best_sale_month(self):
        return max(self.monthly_sales, key=self.monthly_sales.get)

    def display_metrics(self):
        avg_sales = self.calculate_average_sale()
        best_month = self.get_best_sale_month()

        print(f"Average Monthly Sales: {avg_sales:.2f}")
        print(f"Month with the Highest Sales: {best_month} ({self.monthly_sales[best_month]:.2f})")

def main():
    analyzer = SalesAnalyzer('sales_data.csv')
    analyzer.read_sales_data()
    while True:
        print("\n--- Sales Analyzer ---")
        print("1. Generate Sales Graph")
        print("2. Calculate Average Sales")
        print("3. Get Best Sales Month")
        print("4. Display All Metrics")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            analyzer.generate_sales_graph()
        elif choice == "2":
            avg = analyzer.calculate_average_sale()
            print(f"Average Monthly Sales: {avg:.2f}")
        elif choice == "3":
            best_month = analyzer.get_best_sale_month()
            print(f"Month with Highest Sales: {best_month}")
        elif choice == "4":
            analyzer.display_metrics()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()

