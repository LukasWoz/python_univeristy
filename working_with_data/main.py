import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:

        with open('cars.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)

    except:
        with open('cars.csv', 'a', newline='') as csv_file:
            fieldnames = ['brand', 'model', 'date', 'fuel/100km']
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(fieldnames)
        with open('cars.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)

    action = ''
    while action != 'e':

        action = input('Select options and confirm with "enter": "a" - adding new data \t "s" - show elements \t "d" - delete element \t "e" - exit: ')
        if action == 'a':
            with open('cars.csv', 'a', newline='') as csv_file:
                # fieldnames = ['brand', 'model', 'date', 'fuel/100km']
                # csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
                csv_writer = csv.writer(csv_file, delimiter=',')
                # csv_writer.writerow(fieldnames)
                # csv_writer.writeheader()

                car_brand = input('enter the car brand:')
                car_model = input('enter the car model:')
                car_production_date = input('enter the car production date:')
                car_fuel_consumption = input('enter the car fuel consumption per 100 km:')
                car = [car_brand, car_model, car_production_date, car_fuel_consumption]
                csv_writer.writerow(car)

        elif action == 's':
            with open('cars.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    print(line)

        elif action == 'd':
            lines = list()
            delete = input("enter the car's model to be deleted:")
            success = False
            #members = input("Please enter a member's name to be deleted.")
            with open('cars.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    lines.append(line)
                    for field in line:
                        if field == delete:
                            lines.remove(line)
                            success = True
            with open('cars.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(lines)

            if success == True:
                print("the entry has been successfully deleted\n\n")
