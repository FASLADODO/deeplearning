/*
 * Copyright (c) 2017 Jadson Santos
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * NormalizeUrls.java 
 * 27 de jun de 2018
 */
package br.ufrn.deeplearning.logprocess;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import br.ufrn.deeplearning.util.CSVUtils;

/**
 * @author Jadson Santos - jadsonjs@gmail.com
 *
 */
public class ChangeUrlsByNumbers {
	
	public final static String DEFAULT_DIRECTORY       = "/Users/jadson/Desktop/";
	public final static String TEST_DATA_DIRECTORY     = DEFAULT_DIRECTORY+"tests/";
	public final static String TRAINING_DATA_DIRECTORY = DEFAULT_DIRECTORY+"training/";
	
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		normalizeData();
	}

	/**
	 * Generate a number form each URL
	 * 
	 * @throws IOException
	 * @throws FileNotFoundException
	 */
	private static void normalizeData() throws IOException, FileNotFoundException {
		
		int sample = 0; // unfortunately just for 1 sample
		
		Set<String> distinctUrls = new HashSet<String>();
		
		////////////////// for training data  ////////////////// 
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
				    String line = br.readLine();
		
				    while (line != null) {
				    		distinctUrls.add( line );
				        line = br.readLine();
				    }
				}	
				
			}else {
				break forfiles;
			}
		}

		//////////////////for training data  //////////////////
		for (int operation = 1; operation <= 10; operation++) {
			
			String csvFile = TEST_DATA_DIRECTORY+"xtest_"+sample+"_"+operation+".csv";
			
			try( BufferedReader br = new BufferedReader(new FileReader(csvFile))  ) {
				String line = br.readLine();

			    while (line != null) {
			    		distinctUrls.add(line);
			    		line = br.readLine();
			    }
			}
		}
		
		
		
		List<String> distinctUrlsList = new ArrayList<String>(distinctUrls);		
		List<Integer> urlsNumberList = genaratedSequencialNumber(distinctUrlsList);
		
		
		
		saveMapingFile(distinctUrlsList, urlsNumberList);
        
        
		/////////    change the url texto to numeric value for training data ///////
		
		forfiles:
		for (int i = 1; i < 1000000; i++) {
			String csvFile = TRAINING_DATA_DIRECTORY+"training_"+i+".csv";
			
			File file = new File(csvFile);
			
			if( file.exists() ) {
				
				FileWriter finalWriter = new FileWriter(  TRAINING_DATA_DIRECTORY+"training_norm_"+i+".csv" );
				
				FileReader fileReader = new FileReader(file);
				
				try(   BufferedReader br = new BufferedReader(fileReader)  ) {
					
					String line = br.readLine();

				    while (line != null) {
				    		int index = distinctUrlsList.indexOf((line));
				    		
				    		int urlNumber = urlsNumberList.get(index);
				    		
			    	        	CSVUtils.writeLine(finalWriter, Arrays.asList( ""+urlNumber)  );
				    		line = br.readLine();
				    }
				    
				}
				
				finalWriter.flush();
				finalWriter.close();
				
			}else {
				break forfiles;
			}
		}
		
        
        /////////    change the url texto to numeric value for test data ///////
        
       
        for (int operation = 1; operation <= 10; operation++) {
			
        	 	FileWriter finalWriter = new FileWriter(  TEST_DATA_DIRECTORY+"xtest_norm_"+sample+"_"+operation+".csv" );

        	 	int steps = 0;
			try(BufferedReader br = new BufferedReader(new FileReader(TEST_DATA_DIRECTORY+"xtest_"+sample+"_"+operation+".csv"))) {
				
				String line = br.readLine();

			    while (line != null) {
			    		int index = distinctUrlsList.indexOf((line));
			    		
			    		int urlNumber = urlsNumberList.get(index);
			    		
		    	        	CSVUtils.writeLine(finalWriter, Arrays.asList( ""+urlNumber)  );
		    	        	steps++;
			    		//System.out.println("distinctUrls.add(line): "+line);
			    		line = br.readLine();
			    }
			}
			
			// complete the 100 times steps  //
			for (int j = steps; j < 100; j++) {
				CSVUtils.writeLine(finalWriter, Arrays.asList( ""+0)  );
			}
			
			finalWriter.flush();
			finalWriter.close();
        }
		
	}

	private static void saveMapingFile(List<String> distinctUrlsList, List<Integer> urlsNumberList) throws IOException {
		// save the mapping to return //
		String csvFile = DEFAULT_DIRECTORY+"urls_maps.csv";
		
		FileWriter writer = new FileWriter(csvFile);

		for (int i = 0; i < distinctUrlsList.size(); i++) {
        		CSVUtils.writeLine(writer, Arrays.asList( ""+distinctUrlsList.get(i), ""+urlsNumberList.get(i))  );
		}
        
        writer.flush();
        writer.close();
	}

	private static List<Integer> genaratedSequencialNumber(List<String> distinctUrlsList) {
		List<Integer> urlsNumberList = new ArrayList<Integer>(distinctUrlsList.size());
		
		int number = 1;
		for (int i = 0; i < distinctUrlsList.size(); i++) {
			urlsNumberList.add(number++);
		}
		return urlsNumberList;
	}
	
	
}
