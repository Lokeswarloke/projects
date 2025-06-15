package BANK;
import java.util.Scanner;
public class Main {
	
	public static void main(String[] args) {
		Account a=new Account();
		BankOperations bo=new BankOperations();
		Scanner sc=new Scanner(System.in);
		while(true) {
		System.out.println("-----WELCOME-----");
		System.out.println("1.Create Account");
		System.out.println("2.Login");
		System.out.println("3.Exit");
		System.out.println("-----------------");
		System.out.println("Enter your choice: ");
		int enter=sc.nextInt();
		switch(enter) {
		case 1:
			System.out.println("Enter the Name: ");
			String n=sc.next();
			a.setName(n);
			System.out.println("Enter the mail: ");
			String em=sc.next();
			a.setEmail(em);
			System.out.println("Enter the Phone_Number: ");
			long ph=sc.nextLong();
			a.setPh_no(ph);
			System.out.println("Enter the Balance: ");
			double bal=sc.nextDouble();
			a.setBalance(bal);
			System.out.println("Enter the Password: ");
			String pass=sc.next();
			a.setPassword(pass);
			bo.createAccount(a);
			break;
		case 2:
			System.out.println("Enter the mail: ");
			em=sc.next();
			System.out.println("Enter the Password: ");
			pass=sc.next();
			Account loggedIn=bo.login(em, pass);
			System.out.println("***Account Logged In***");
			if(loggedIn!=null) {
				boolean b=true;
				while(b) {
				System.out.println("1. Withdraw");
				System.out.println("2. Deposit");
				System.out.println("3. Check Balance");
				System.out.println("4. Exit");
				System.out.println("Enter your option in above Transactions");
				int input=sc.nextInt();
				switch(input) {
				case 1:
					System.out.println("Welcome to Withraw function");
					bo.withdraw(a);
					break;
				case 2:
					bo.deposit(a);
					break;
				case 3:
					bo.CheckBalance(a);
					break;
				case 4:
					System.out.println("***Account logged out***");
					b=false;
					break;
				}
			}
				
			}
			
		case 3:
			System.out.println("Thank You");
			System.exit(0);
		}

		
		}
	}

}
