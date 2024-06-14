import pandas as pd
import matplotlib.pyplot as plt

# Load data
lwd = pd.read_csv("livwell135.csv")

# Check and print column names
print("Column names in the dataset:")
print(lwd.columns)

def show_intro():
    print("Welcome to the Peru Women's Employment and Income Data Analysis Tool!")
    print("There are a total of 15.89 million women in Peru. 66.09% are employed in the workforce and are of working age.\n")

def show_menu():
    print("Please choose an option:")
    print("1. Show percentage of women earning more than their partners over the years")
    print("2. Show employment rate over the years")
    print("3. Show data summary")
    print("4. Exit")

def show_women_earning_more():
    oneCountryBooleanList = lwd["country_name"] == "Peru"
    oneCountryData = lwd.loc[oneCountryBooleanList]

    plt.title("Percentage of Women Earning More than their Partners")
    plt.xlabel("Year")
    plt.ylabel("Women Earning More than their Partners (%)")
    plt.scatter(x="year", y="DP_earn_more_p", data=oneCountryData)
    plt.ylim(0, 20)
    plt.show()

    print("According to the graph, the amount of women earning more than their partners is 14%+ from 2004-2008, however, there was a brief dip from between 2008-2012. While the percentage is slowly rising, as of the middle of 2010, it is still far below the average from the previous years.\n")
    print("This difference could be due to many reasons such as: culture, work requirements, health issues, and the still-present issue of sexism. However, as the country continues to grow, so does the amount of women who are striving for more independence and face less discrimination.\n")
    print("All in all, although progress has been made, we as a society are still far behind and should push ourselves through barriers and fight for equality and rightful equity.")

def show_employment_rate():
    oneCountryBooleanList = lwd["country_name"] == "Peru"
    oneCountryData = lwd.loc[oneCountryBooleanList]

    # Adjust the column name to match your data
    plt.title("Employment Rate of Women in Peru")
    plt.xlabel("Year")
    plt.ylabel("Employment Rate (%)")
    
    if "employment_rate" in oneCountryData.columns:
        plt.plot(oneCountryData["year"], oneCountryData["employment_rate"], marker='o')
    elif "employment_rate_percent" in oneCountryData.columns:  # Example alternative column name
        plt.plot(oneCountryData["year"], oneCountryData["employment_rate_percent"], marker='o')
    else:
        print("Employment rate column not found in the dataset.")
        return
    
    plt.ylim(0, 100)
    plt.show()

    print("The employment rate of women in Peru has been visualized in the graph above. Analyze the trends to understand how employment rates have changed over the years.\n")

def show_data_summary():
    oneCountryBooleanList = lwd["country_name"] == "Peru"
    oneCountryData = lwd.loc[oneCountryBooleanList]
    summary = oneCountryData.describe()
    print("Data Summary for Women in Peru:")
    print(summary)

def main():
    show_intro()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            show_women_earning_more()
        elif choice == '2':
            show_employment_rate()
        elif choice == '3':
            show_data_summary()
        elif choice == '4':
            print("Thank you for using the tool! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
