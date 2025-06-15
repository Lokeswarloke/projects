package BANK;
import java.util.*;
public class BankOperations {
	Scanner sc=new Scanner(System.in);
	ArrayList<Account> arr=new ArrayList<Account>();
	public void createAccount(Account a) {
			arr.add(a);
			System.out.println("**Account Created Successfully**");
		}
		
	public Account login(String mail, String pass) {
		for(Account a:arr) {
			if(a.email.equals(mail) && a.password.equals(pass)) {
				System.out.println("Login Success");
				return a;
			}
			else {
				System.out.println("The input combination doesnot exists, !Enter valid details");
			}
		}
		return null;
	}
	public void withdraw(Account ref) {
		System.out.println("Enter the withdraw amount");
		double amount=sc.nextInt();
		double bal=ref.getBalance();
		if(amount<bal) {
			bal=bal-amount;
			ref.setBalance(bal);
			System.out.println("Amount successfully withdrawn");
		}
		else {
			System.out.println("Insufficient Balance");
		}
	}
	public void CheckBalance(Account ref1) {
		System.out.println("Balance amount is: "+ref1.getBalance());
	}
	public void deposit(Account ref2) {
		System.out.println("Enter the amount to deposit");
		double amount1=sc.nextInt();
		
		if(amount1<=0) {
			System.out.println("Enter the invalid amount");
			
		}
		else {
			double bal1=ref2.getBalance();
			bal1=bal1+amount1;
			ref2.setBalance(bal1);
			System.out.println("Deoposited Successfully");
			
			
		}
	}
	
}
