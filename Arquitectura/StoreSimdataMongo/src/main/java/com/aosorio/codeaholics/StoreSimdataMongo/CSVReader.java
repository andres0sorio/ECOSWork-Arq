package com.aosorio.codeaholics.StoreSimdataMongo;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * This is a simple CSV reader. Input must be in the form of columns, each
 * column separated by a , (comma). Given we have to work out data in columns in
 * terms of Linked Lists there is a method to provide the data in such form.
 */

public class CSVReader {

	private String inputFile;

	BufferedReader buffer = null;

	String cvsSplitBy = ",";
	int nrow = 0;

	public CSVReader(String infile) {
		inputFile = infile;
	}

	public void readFile(ArrayList<JsonEpisodeHelper> records) {

		try {

			buffer = new BufferedReader(new FileReader(inputFile));

			String line;

			while ((line = buffer.readLine()) != null) {

				String[] data = line.split(cvsSplitBy);

				JsonEpisodeHelper record = new JsonEpisodeHelper();

				record.setCedula(Integer.parseInt(data[0]));
				record.setFecha(data[1]);
				record.setHora(data[2]);
				record.setNivelDolor(Integer.parseInt(data[3]));
				record.setMedicamento(data[4]);
				record.setActividad(data[5]);

				records.add(record);

				nrow++;

			}

		} catch (FileNotFoundException e) {
			System.out.println("File not found, please check!");
		} catch (IOException e) {
			System.out.println("IO error, please check!");
		} finally {
			if (buffer != null) {
				try {
					if (nrow == 0)
						System.out.println("Current file is empty. Nothing to do.");
					else
						System.out.println("End of file reached, success.");
					buffer.close();
				} catch (IOException e) {
					System.out.println("IO error at closing file.");
				}
			}
		}
	}

}
