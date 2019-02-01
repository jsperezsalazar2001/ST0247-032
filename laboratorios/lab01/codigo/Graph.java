/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author cl18405
 */
public class Graph {

    public void readGrahp(String fileName) {
        BufferedReader reader = null;
        try {
            File file = new File(fileName);
            reader = new BufferedReader(new FileReader(file));
            String line;
            line = reader.readLine();
            while ((line = reader.readLine()) != null) {
                if (!line.equals("")) {
                    if (line.contains("Arco")) {
                        break;
                    }
                    String[] lineArray = line.split(" ");
                    Node node = new Node(lineArray[0], Double.parseDouble(lineArray[1]), Double.parseDouble(lineArray[2]), lineArray[3]);
                }
            }
            while ((line = reader.readLine()) != null) {
                if (!line.equals("")) {
                    String[] lineArray = line.split(" ");
                    Arc arc = new Arc(lineArray[0], lineArray[0], Integer.parseInt(lineArray[2]), lineArray[3]);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {

    }

}
