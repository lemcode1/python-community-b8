import logging

logging.basicConfig(level=logging.DEBUG, filename='pb8_logging.log', format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# logging.debug("This is debug message") # 10
# logging.info("This is info message")   # 20
# logging.warning("This is warning message") # 30
# logging.error("This is error message")  # 40
# logging.critical("This is critical message") # 50
a=int(input("Enter a value"))
b=int(input("Enter b value"))

try:
    logging.info(f"A value is {a}")
    logging.info(f"B value is {b}")
    c=a/b
    print("C value is ",c)
except Exception as e:
    logging.error(f"Error while dividing {e}", exc_info=True)