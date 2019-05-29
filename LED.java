public class LED {
	public static void main(String[] args) {
		int blinkCount = 3;
		int count = 0;
		boolean yellow, blue, green, red;
		
		while(count < blinkCount) {
			yellow = true;
			green = false;
			red = false;
			blue = true;
			System.out.println("GROUP 1 ON");
			yellow = false;
			green = true;
			red = true;
			blue = false;
			System.out.println("GROUP 2 ON");
			yellow = false;
			green = false;
			red = false;
			blue = false;
		}
	}
	
}
