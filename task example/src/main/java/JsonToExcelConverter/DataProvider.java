package JsonToExcelConverter;

import java.util.ArrayList;
import java.util.List;

public class DataProvider {
    private List<String> sheetHeader = new ArrayList<>();
    private List<String> nameOfTheStudent = new ArrayList<>();
    private List<Integer> ageOfTheStudent = new ArrayList<>();
    private List<Integer> totalMarksOfTheStudent = new ArrayList<>();

    public List<String> getSheetHeader() {
        return sheetHeader;
    }

    public void setSheetHeader(List<String> sheetHeader) {
        this.sheetHeader = sheetHeader;
    }

    public List<String> getNameOfTheStudent() {
        return nameOfTheStudent;
    }

    public void setNameOfTheStudent(List<String> nameOfTheStudent) {
        this.nameOfTheStudent = nameOfTheStudent;
    }

    public List<Integer> getAgeOfTheStudent() {
        return ageOfTheStudent;
    }

    public void setAgeOfTheStudent(List<Integer> ageOfTheStudent) {
        this.ageOfTheStudent = ageOfTheStudent;
    }

    public List<Integer> getTotalMarksOfTheStudent() {
        return totalMarksOfTheStudent;
    }

    public void setTotalMarksOfTheStudent(List<Integer> totalMarksOfTheStudent) {
        this.totalMarksOfTheStudent = totalMarksOfTheStudent;
    }
}

