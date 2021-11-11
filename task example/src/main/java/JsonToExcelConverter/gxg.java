package JsonToExcelConverter;


import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Implementor extends DataProvider  {
    String excelFilePath = "C:\\Users\\zenith\\Desktop\\jenith1.xlsx";

    public void readTheJsonFile() {
        List<String> sheetHeader = new ArrayList<>();
        List<String> nameOfTheStudent = new ArrayList<>();
        List<Integer> ageOfTheStudent = new ArrayList<>();
        List<Integer> totalMarksOfTheStudent = new ArrayList<>();
        String columnOne = "Name";
        String columnTwo = "Age";
        String columnThree = "Total Marks";
        sheetHeader.add(columnOne);
        sheetHeader.add(columnTwo);
        sheetHeader.add(columnThree);
        try {
            System.out.println("Reading the JSON file...");
            JSONParser parser = new JSONParser();
            FileReader fileReader = new FileReader(new File("C:\\Users\\zenith\\task example\\src\\test\\task.json"));
            Object object = parser.parse(fileReader);
            JSONArray studentRecords = (JSONArray) object;
            for (Object recordObjects : studentRecords) {
                JSONObject student = (JSONObject) recordObjects;
                String name = (String) student.get(columnOne);
                nameOfTheStudent.add(name);
                int age = Integer.parseInt(student.get(columnTwo).toString());
                ageOfTheStudent.add(age);
                int marks = Integer.parseInt(student.get(columnThree).toString());
                totalMarksOfTheStudent.add(marks);
            }
            setSheetHeader(sheetHeader);
            setNameOfTheStudent(nameOfTheStudent);
            setAgeOfTheStudent(ageOfTheStudent);
            setTotalMarksOfTheStudent(totalMarksOfTheStudent);

        } catch (FileNotFoundException exception) {
            System.out.println("Check, if the file is present in the given path!");
        } catch (IOException | ParseException exception) {
            System.out.println("Check the file in the specified path.");
        }
    }

    public void generateTheExcelFile() {

        try {
            System.out.println("Generating the Excel file....");
            File fileObject = new File(excelFilePath);
            FileOutputStream writerObject = new FileOutputStream(fileObject);
            XSSFWorkbook workBook = new XSSFWorkbook();
            XSSFSheet sheet = workBook.createSheet("Student Records");
            int numberOfRows = getNameOfTheStudent().size()+1;
            int numberOfColumns = getSheetHeader().size();
            Row sheetHeader = sheet.createRow(0);
            for (int columnIndex = 0; columnIndex < numberOfColumns; columnIndex++) {
                if (columnIndex == 0) {
                    Cell cellData = sheetHeader.createCell(columnIndex);
                    cellData.setCellValue(getSheetHeader().get(columnIndex));
                } else if (columnIndex == 1) {
                    Cell cellData = sheetHeader.createCell(columnIndex);
                    cellData.setCellValue(getSheetHeader().get(columnIndex));
                } else if (columnIndex == 2) {
                    Cell cellData = sheetHeader.createCell(columnIndex);
                    cellData.setCellValue(getSheetHeader().get(columnIndex));
                }
            }
            for (int rowIndex = 1; rowIndex < numberOfRows; rowIndex++) {
                Row rowData = sheet.createRow(rowIndex);
                for (int columnIndex = 0; columnIndex < numberOfColumns; columnIndex++) {
                    if (columnIndex == 0) {
                        Cell columnOne = rowData.createCell(columnIndex);
                        columnOne.setCellValue(getNameOfTheStudent().get(rowIndex-1));
                    } else if (columnIndex == 1) {
                        Cell columnTwo = rowData.createCell(columnIndex);
                        columnTwo.setCellValue(getAgeOfTheStudent().get(rowIndex-1));
                    } else if (columnIndex == 2) {
                        Cell columnThree = rowData.createCell(columnIndex);
                        columnThree.setCellValue(getTotalMarksOfTheStudent().get(rowIndex-1));
                    }
                }
            }
            workBook.write(writerObject);
            System.out.println("Excel file generated successfully");
        } catch (IOException exception) {
            System.out.println("Check the file in the specified path.");
        }
    }
}
