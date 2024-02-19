
CREATE database bvm;
use bvm;
CREATE TABLE IF NOT EXISTS students (        
        name VARCHAR(40),
        father_name VARCHAR(40),
        mother_name VARCHAR(40),
        srn_no VARCHAR(255) PRIMARY KEY,
        pen_no VARCHAR(40),
        admission_no VARCHAR(40),
        class VARCHAR(40),
        session VARCHAR(40),
        roll VARCHAR(40)
    );
    
CREATE TABLE IF NOT EXISTS pdf_files (
        srn_no VARCHAR(255) PRIMARY KEY,
        pdf_data LONGBLOB,
        FOREIGN KEY(srn_no) REFERENCES students(srn_no)
    );

CREATE TABLE IF NOT EXISTS question_paper_table (
        class VARCHAR(255),
        session VARCHAR(255),
        term VARCHAR(40),
        subjects VARCHAR(100),
        pdf_paper LONGBLOB,
        PRIMARY KEY(class, session, term, subjects)
    );

CREATE TABLE IF NOT EXISTS photo(
        id VARCHAR(255) PRIMARY KEY, 
        image LONGBLOB,
        FOREIGN KEY(id) REFERENCES students(srn_no));
        
CREATE TABLE IF NOT EXISTS marks1(
        id VARCHAR(255) PRIMARY KEY, 
        english1 INTEGER NOT NULL,
        hindi1 INTEGER NOT NULL,
        mathematics1 INTEGER NOT NULL,
        social_science1 INTEGER NOT NULL,
        science1 INTEGER NOT NULL,
        computer1 INTEGER NOT NULL,
        drawing1 VARCHAR(50) NOT NULL,
        gn1 INTEGER NOT NULL,
        grandTotal1 INTEGER ,
        percentage1 DECIMAL(10, 2),
        rank1 VARCHAR(50),
        
        FOREIGN KEY(id) REFERENCES students(srn_no));
CREATE TABLE IF NOT EXISTS marks2(
        id VARCHAR(255) PRIMARY KEY, 
        english2 INTEGER NOT NULL,
        hindi2 INTEGER NOT NULL,
        mathematics2 INTEGER NOT NULL,
        social_science2 INTEGER NOT NULL,
        science2 INTEGER NOT NULL,
        computer2 INTEGER NOT NULL,
        drawing2 VARCHAR(50) NOT NULL,
        gn2 INTEGER NOT NULL,
        grandTotal2 INTEGER NOT NULL,
        percentage2 DECIMAL(10, 2),
        rank2 VARCHAR(50),
        
        FOREIGN KEY(id) REFERENCES students(srn_no));
CREATE TABLE IF NOT EXISTS marks3(
        id VARCHAR(255) PRIMARY KEY, 
        english3 INTEGER NOT NULL,
        hindi3 INTEGER NOT NULL,
        mathematics3 INTEGER NOT NULL,
        social_science3 INTEGER NOT NULL,
        science3 INTEGER NOT NULL,
        computer3 INTEGER NOT NULL,
        drawing3 VARCHAR(50) NOT NULL,
        gn3 INTEGER NOT NULL,
        grandTotal3 INTEGER NOT NULL,
        percentage3 DECIMAL(10, 2),
        rank3 VARCHAR(50),
        
        FOREIGN KEY(id) REFERENCES students(srn_no));

CREATE TABLE IF NOT EXISTS maximum_marks(
        id VARCHAR(255) PRIMARY KEY, 
        maxEng INTEGER NOT NULL,        
        maxHindi INTEGER NOT NULL,        
        maxMaths INTEGER NOT NULL,        
        maxSst INTEGER NOT NULL,        
        maxScience INTEGER NOT NULL,        
        maxComp INTEGER NOT NULL,        
        maxDrawing VARCHAR(50) NOT NULL,
        maxGn INTEGER NOT NULL,        
        maxGrandTotal INTEGER NOT NULL,        
        attendance VARCHAR(50),
        maxRank VARCHAR(50),
          
   
        FOREIGN KEY(id) REFERENCES students(srn_no));
        