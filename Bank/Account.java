package BANK;

public class Account {
	String name;
	String email;
	long ph_no;
	double balance;
	String password;
	public void setName(String name) {
		this.name = name;
	}
	public String getName() {
		return name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public long getPh_no() {
		return ph_no;
	}
	public void setPh_no(long ph_no) {
		int count=0;
		while(ph_no!=0) {
			ph_no=ph_no/10;
			count++;
		}
		if(count==10) {
			this.ph_no = ph_no;
		}
		else {
			System.err.println("Enter correct mobile num");
		}
	}
	public double getBalance() {
		return balance;
	}
	public void setBalance(double balance) {
		this.balance = balance;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	
}
