# PAYMENT TYPE CHOICES:
PAYME = "uzcard"
APELSIN = "apelsin"
VISA = "visa"
CLICK = 'click'
MASTERCARD = 'mastercard'
KPAY = 'kpay'
CASH = 'cash'

PAYMENT_TYPE_CHOICES = (
    (PAYME, "payme"),
    (APELSIN, "apelsin"),
    (VISA, "visa"),
    (CLICK, 'click'),
    (MASTERCARD, 'mastercard'),
    (KPAY, 'kpay'),
    (CASH, "cash"),
)

# GENDER TYPE CHOICES:
MAN = "man"
FEMALE = "female"

GENDER_TYPE_CHOICES = (
    (MAN, "man"),
    (FEMALE, "female"),
)

# BADGE TYPE CHOICES
BESTSELLER = "bestseller"
RECOMMENDED = "recommended"

BADGE_TYPE_CHOICES = (
    (BESTSELLER, "bestseller"),
    (RECOMMENDED, "recommended"),

)

# PAYMENT STATUS TYPE CHOICES
PURCHASED = "purchased"
NOT_PURCHASED = "not puchased"
IN_PROGRESS = "in progres"

PAYMENT_STATUS_CHOICES = (
    (NOT_PURCHASED, "not puchased"),
    (IN_PROGRESS, "in progres"),
    (PURCHASED, "purchased"),
)

# COURSE COMMENT STATUS TYPE CHOICES
ACTIVE = "active"
PENDING = "pending"
DENIED = "denied"

COURSE_COMMENT_STATUS_TYPE_CHOICES = (
    (ACTIVE, "active"),
    (PENDING, "pending"),
    (DENIED, "denied"),
)

# LECTURE COMMENT STATUS TYPE CHOICES
ACTIVE = "active"
PENDING = "pending"
DENIED = "denied"

LECTURE_COMMENT_STATUS_TYPE_CHOICES = (
    (ACTIVE, "active"),
    (PENDING, "pending"),
    (DENIED, "denied"),
)

# USER AUTH STATUS
NEW, PHONE_ENTERED, CODE_VERIFIED, AUTH_DONE = (
    "NEW",
    "PHONE_ENTERED",
    "CODE_VERIFIED",
    "DONE"
)

AUTH_STATUS = (
        (NEW, NEW),
        (PHONE_ENTERED, PHONE_ENTERED),
        (CODE_VERIFIED, CODE_VERIFIED),
        (AUTH_DONE, AUTH_DONE)
)
