from helpers.rand_gen import random_with_n_digits

# REQUISITES
OGRN = "5087746145383"
INN = "7743707160"
KPP = str(random_with_n_digits(9))
RUSSIA_CODE = "RUS"
PHONE = f"7{random_with_n_digits(10)}"
EMAIL = "test@test.com"
ADDRESS = f"Москва, Очаковская, {random_with_n_digits(3)}"
POSTAL_ADDRESS = f"Москва, Обуховская, {random_with_n_digits(3)}"
BANK_DEPT = "Очаково"
BANK_NAME = "СБЕРБАНК РОССИИ"
PAYMENT_ACCOUNT = str(random_with_n_digits(20))
CORR_ACCOUNT = str(random_with_n_digits(20))
BIC = str(random_with_n_digits(9))

# ERRORS
KPP_ERROR = "Kpp is required"
ADDRESS_ERROR = "Укажите юридический адрес"
PHONE_ERROR = "Phone is required"
EMAIL_ERROR = "Email is required"
BANK_DEPT_ERROR = "Name bank is required"
PAYMENT_ACCOUNT_ERROR = "Payment account is required"
CORR_ACCOUNT_ERROR = "Correspondent account is required"
BIC_ERROR = "BIC is required"
