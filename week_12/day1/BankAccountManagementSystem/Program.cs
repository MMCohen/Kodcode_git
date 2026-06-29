using Microsoft.VisualBasic;

namespace Bank
{
    enum AccountTypeEnum { Savings, Checking, Business}

    class BankAccount
    {
        private int _accountNumber { get;}
        private string _ownerName { get; set; }
        private double _balance;
        private string _accountType;
        private bool _isActive;
        private List<string> _transactionHistory = new();
        
        public int AccountNumber // TODO: does it needs to be unique
        {
            get => _accountNumber;
        }
        public string OwnerName
        {
            get => _ownerName;
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    _ownerName = "Unknown";
                }
                else _ownerName = value;
            }
        }
        public double Balance 
        {
            get => _balance;
            set
            {
                if (value < 0)
                {
                    _balance = 0;
                }
                else
                {
                    _balance = value;
                }
            }
        }
        public string AccountType
        {
            get => _accountType;
            set
            {
                if (Enum.TryParse(value,ignoreCase: true , out AccountTypeEnum acc))
                {
                    _accountType = acc.ToString();
                }
                else
                {
                    _accountType = "Checking";
                }
            }
        }
        public bool IsActive
        {
            get => _isActive;
            private set
            {
                _isActive = value;
            }
        }
        public void Deactivate() {IsActive = false;}
        public void Activate() {IsActive = true;}

        public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
        {
            _accountNumber = accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;
            IsActive = true;
            Console.WriteLine("hello from MAIN constrator");
        }

        public BankAccount(int accountNumber, string ownerName) : this(accountNumber, ownerName, 0.0, "Checking")
        {
            Console.WriteLine("hello from OVERLOAD constrator");
        }

        public override string ToString()
        {
            return $"Account #{_accountNumber} | Owner: {_ownerName} | Balance: ${_balance:F2} | Type: {_accountType}";
        }

        public void Deposit(double DepositAmount)
        {
            if (DepositAmount < 0)
            {
                Console.WriteLine("Amount must be positive");
                return;
            }
            _balance += DepositAmount;
            Console.WriteLine("Deposit successfully");
            _transactionHistory.Add($"Deposit {DepositAmount}$");
            return;
        }
        public bool Withdraw(double WithdrawAmount)
        {
            if (WithdrawAmount < 0)
            {
                Console.WriteLine("Withdraw amount must be positive");
                return false;
            }

            if (WithdrawAmount > _balance)
            {
                Console.WriteLine("Balance must be sufficient");
                return false;
            }

            _balance -= WithdrawAmount;
            _transactionHistory.Add($"Withdraw {WithdrawAmount}$");
            return true;
        }

        public void ApplyInterest()
        {
            if (_accountType.ToLower() == "savings")
            {
                _balance = _balance * 1.02;
            }
        }

        public void PrintTransactionHistory()
        {
            for (int i = 0; i < _transactionHistory.Count(); i++)
            {
                Console.WriteLine(_transactionHistory[i]);
            }
        }


    }

    class program
    {
        static void Main()
        {
            //BankAccount ba1 = new BankAccount(12345, " ", -6, "savings");
            BankAccount ba2 = new BankAccount(12345, "Moshe", 0.0, "savings");
            Console.WriteLine(ba2);
            ba2.Deposit(100);
            ba2.Deposit(100);
            ba2.Deposit(100);
            ba2.Withdraw(222);
            Console.WriteLine(ba2);
            ba2.ApplyInterest();
            Console.WriteLine(ba2);
            ba2.PrintTransactionHistory();
            



        }
    }
}