/*
Author Madan Ram
Email id: madan_ram@rocketmail.com
This file is part of GoLamper (FS)Freadom Software LTD (founder Madan Ram).

    GoLamper is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

*/
import java.util.*;

public class StringMatchWithGap {

	public static class arrowType {
		public static final int TILT = 1;
		public static final int LEFT = 2;
		public static final int UP = 3;
	}

	private static int[][] addTiltArrow(String s1,String s2) {
		int[][] arrowMatrix = new int[s2.length()+1][s1.length()+1];
		for(int i=0;i<s2.length();i++) {
			for(int j=0;j<s1.length();j++) {
				if(s1.charAt(j)==s2.charAt(i)) arrowMatrix[i+1][j+1]=1;
			}
		}
		return arrowMatrix;
	}

	private static int[] fillArrowMatrix(int[][] arrowMatrix) {

		int[][] countMatrix=new int[arrowMatrix.length][arrowMatrix[0].length];
		for(int i=1;i<arrowMatrix.length;i++) {
			for(int j=1;j<arrowMatrix[0].length;j++) {
				if(arrowMatrix[i][j]!=arrowType.TILT) {
					if(countMatrix[i-1][j]>=countMatrix[i][j-1]) {
						countMatrix[i][j]=countMatrix[i-1][j];
						arrowMatrix[i][j]=arrowType.UP;
					} else {
						countMatrix[i][j]=countMatrix[i][j-1];
						arrowMatrix[i][j]=arrowType.LEFT;
					}
				} else {
					countMatrix[i][j]=countMatrix[i-1][j-1]+1;
				}
			}
		}
		int[] foundLengths=countMatrix[countMatrix.length-1];
		countMatrix=null;
		return foundLengths;
	}

	private static void printMatrix(int[][] a) {
		for(int i=0;i<a.length;i++) {
			for(int j=0;j<a[0].length;j++) {
				System.out.print(a[i][j]+"	");
			}
			System.out.println();
		}
	}

	private static void printArray(int[] a,int n) {
		for(int i=0;i<n;i++) {
			System.out.print(a[i]+"	");
		}
		System.out.println();
	}

	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int tests1=Integer.parseInt(scan.next());
		int[] foundLengths;
		while((tests1--)!=0) {
			String s1=scan.next();
			int tests2=Integer.parseInt(scan.next());
			while(tests2--!=0) {
				String s2=scan.next();
				boolean found=false;
				int posStart=0;
				int posEnd=0;
				int countLength=0;
				int minPosEnd=0;
				int minPosStart=0;
				int left=0;
				int top=0;
				int minCountLength=9999;
				int[][] arrowMatrix=addTiltArrow(s1,s2);
				foundLengths=fillArrowMatrix(arrowMatrix);
				//printMatrix(arrowMatrix);
				//System.out.println("-----------------------------------------------");
				//printArray(foundLengths,foundLengths.length);
				for(int i=1;i<foundLengths.length;i++) {
					left=i;
					top=arrowMatrix.length-1;
					if(foundLengths[i]==s2.length() && arrowMatrix[top][i]==arrowType.TILT) {
						countLength=0;
						while(top>0 && left>0) {
							countLength++;
							if(arrowMatrix[top][left]==arrowType.TILT) {
								top=top-1;
								left=left-1;
							} else if(arrowMatrix[top][left]==arrowType.LEFT) {
								left=left-1;
							} else if(arrowMatrix[top][left]==arrowType.UP) {
								top=top-1;
							}
						}

						if(minCountLength>countLength) {
							found=true;
							minCountLength=countLength;
							minPosEnd=i;
							minPosStart=minPosEnd - countLength+1;
						}

					}
				}
				if(found)
					System.out.println(minPosStart+","+minPosEnd);
				else System.out.println(-1);
			}

		}
			
	}
}