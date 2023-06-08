""" 
Description: 
  Divides sales data CSV file into individual order data Excel files.

Usage:
  python process_sales_data.py sales_csv_path

Parameters:
  sales_csv_path = Full path of the sales data CSV file
"""

import pandas as pd
import sys
import os.path
from datetime import date


def main():
    sales_csv_path = get_sales_csv_path()
    orders_dir_path = create_orders_dir(sales_csv_path)
    process_sales_data(sales_csv_path, orders_dir_path)

def get_sales_csv_path():
    """Gets the path of sales data CSV file from the command line

    Returns:
        str: Path of sales data CSV file
    """
    # TODO: Check whether command line parameter provided
    num_params = len(sys.argv) - 1
    if num_params < 1:
        print("Error: Missing CSV path parameter.")
        sys.exit()


    # TODO: Check whether provide parameter is valid path of file
    csv_path = sys.argv[1]
    if not os.path.isfile(csv_path):
        print("Error: CSV path is not an existing file.")
        sys.exit()


    # TODO: Return path of sales data CSV file
    return os.path.abspath(csv_path) 
    

def create_orders_dir(sales_csv_path):
    """Creates the directory to hold the individual order Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file

    Returns:
        str: Path of orders directory
    """
    # TODO: Get directory in which sales data CSV file resides
    sales_csv_dir = os.path.dirname(sales_csv_path)
    # TODO: Determine the path of the directory to hold the order data files
    
    today_date = date.today().isoformat()
    orders_dir = f'orders_{today_date}'
    orders_dir_path = os.path.join(sales_csv_dir, orders_dir)

    # TODO: Create the orders directory if it does not already exist


    # TODO: Return path of orders directory
    return

def process_sales_data(sales_csv_path, orders_dir_path):
    """Splits the sales data into individual orders and save to Excel sheets

    Args:
        sales_csv_path (str): Path of sales data CSV file
        orders_dir_path (str): Path of orders directory
    """
    # TODO: Import the sales data from the CSV file into a DataFrame
    # TODO: Insert a new "TOTAL PRICE" column into the DataFrame
    # TODO: Remove columns from the DataFrame that are not needed
    # TODO: Groups orders by ID and iterate 
        # TODO: Remove the 'ORDER ID' column
        # TODO: Sort the items by item number
        # TODO: Append a "GRAND TOTAL" row
        # TODO: Determine the file name and full path of the Excel sheet
        # TODO: Export the data to an Excel sheet
        # TODO: Format the Excel sheet
        # TODO: Define format for the money columns
        # TODO: Format each colunm
        # TODO: Close the Excelwriter 
    return

if __name__ == '__main__':
    main()