public class Initials {
	public static void main(String[] args){
		// use 32-bits int to represent the matrix 0 and 1
		// the dump thing is that I translated those bytes by myself
		int[] iArray = {
			0xc0387fe0, 0x60008003,
			0xc0e06018, 0x3001c006,
			0xc380600c, 0x1803600c,
			0xce006006, 0x0c063018,
			0xf8006006, 0x060c1830,
			0xce006006, 0x03180c60,
			0xc380600c, 0x01b006c0,
			0xc0e06018, 0x00e00380,
			0xc0387fe0, 0x00400100
		};

		int i = 0;
		while(i < iArray.length){
			if (i%2 == 0 && i != 0) {
				System.out.println();
			}
			int temp = iArray[i];
			for (int k = 0; k < 32; k++) {
				if ((temp & 0x80000000) == 0) {
					System.out.print(' ');
				}
				else {
					System.out.print('*');
				}
				temp = temp << 1;
			}
			i++;
		}
		System.out.println();
	}
}
