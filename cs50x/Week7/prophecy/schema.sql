CREATE TABLE student (
    id INTEGER,
    student_name TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    house TEXT,
    PRIMARY KEY(house)
);

CREATE TABLE link (
    student_id INTEGER,
    student_house TEXT,
    FOREIGN KEY(student_id) REFERENCES student (id),
    FOREIGN KEY(student_house) REFERENCES houses(house)
);
