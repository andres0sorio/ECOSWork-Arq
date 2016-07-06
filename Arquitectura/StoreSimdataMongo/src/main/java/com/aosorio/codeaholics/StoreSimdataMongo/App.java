package com.aosorio.codeaholics.StoreSimdataMongo;

import java.net.URL;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.Iterator;
import java.io.*;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * Hello world!
 *
 */
public class App {
	
	private static ArrayList<JsonEpisodeHelper> listOfEpisodes;
	private static JsonEpisodeHelper data;
	
	public static void main(String[] args) throws Exception {

		//System.setProperty("javax.net.ssl.keyStore", "deploy/keystore.jks");
		//System.setProperty("javax.net.ssl.keyStorePassword","password");
		
		System.out.println("Hello World!");
		listOfEpisodes = new ArrayList<JsonEpisodeHelper>();
		int nepisodes = getEpisodes( );
		System.out.println("Total imported episodes> " + nepisodes);
		
		String httpsURL = "https://157.253.17.148:4567/api/episode/create";
		URL myurl = new URL(httpsURL);

		int HttpResult = 0;

		Gson GSON = new GsonBuilder().create();

		Iterator<JsonEpisodeHelper> episode = listOfEpisodes.iterator();
    	
        while( episode.hasNext() ) {
        	
        	HttpsURLConnection urlConnection = (HttpsURLConnection) myurl.openConnection();
    		urlConnection.setDoOutput (true);
    		urlConnection.setUseCaches (false);
    		urlConnection.setRequestProperty("Content-Type", "application/json");
    		urlConnection.setRequestMethod("POST");
    		
        	HttpResult = 0;
        	
        	data = episode.next();

            String JsonDATA = GSON.toJson(data).toString();
            
            Writer writer = new BufferedWriter(new OutputStreamWriter(urlConnection.getOutputStream(), "UTF-8"));

            writer.write(JsonDATA);
            writer.flush();
            HttpResult = urlConnection.getResponseCode();

            if (HttpResult == 200) {
                System.out.println("Success!");
            }

        }
		
	}

	private static int getEpisodes() {
		//Auto-generated method stub
		int counter = 0;
		
		CSVReader csvreader = new CSVReader("simulated_records.dat");
		csvreader.readFile( listOfEpisodes );
		counter = listOfEpisodes.size();
		
		return counter;
	}
	
	static {
	    disableSslVerification();
	}

	private static void disableSslVerification() {
	    try
	    {
	        // Create a trust manager that does not validate certificate chains
	        TrustManager[] trustAllCerts = new TrustManager[] {new X509TrustManager() {
	            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
	                return null;
	            }
	            public void checkClientTrusted(X509Certificate[] certs, String authType) {
	            }
	            public void checkServerTrusted(X509Certificate[] certs, String authType) {
	            }
	        }
	        };

	        // Install the all-trusting trust manager
	        SSLContext sc = SSLContext.getInstance("SSL");
	        sc.init(null, trustAllCerts, new java.security.SecureRandom());
	        HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

	        // Create all-trusting host name verifier
	        HostnameVerifier allHostsValid = new HostnameVerifier() {
	            public boolean verify(String hostname, SSLSession session) {
	                return true;
	            }
	        };

	        // Install the all-trusting host verifier
	        HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);
	    } catch (NoSuchAlgorithmException e) {
	        e.printStackTrace();
	    } catch (KeyManagementException e) {
	        e.printStackTrace();
	    }
	}
	

}



