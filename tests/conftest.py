import pytest
from asciidoc.mocks import *


@pytest.fixture(scope="class")
def normal_data():
    diagram = None
    diagram = TestDiagram()

    fk1 = TestForeignKey()
    fkcol1 = TestForeignKeyColumn()
    fkcol1.name = 'PK column'
    fk1.columns.append(fkcol1)
    fkrefcol1 = TestForeignKeyReferenceColumn()
    fkrefcol1.name = 'fk ref col name'
    fkrefcol1.owner.name = 'owner name'
    fk1.referencedColumns.append(fkrefcol1)

    idx1 = TestIndex()
    idx1.name = "PK index"
    idx1.columns = []
    idx1.indexType = "PRIMARY"
    idx1.comment = "some comment"

    idxcol1 = TestIndexColumn()
    idxcol1.referencedColumn.name = "PK column"
    idx1.columns.append(idxcol1)

    idxcol2 = TestIndexColumn()
    idxcol2.referencedColumn.name = "colname"
    idx1.columns.append(idxcol2)

    col1 = TestColumn()
    col1.name = "PK column"
    col1.autoIncrement = 1
    col1.isNotNull = 1
    col1.simpleType.name = "VARCHAR"
    col1.length = "2"
    col1.defaultValue = "default value"
    col1.comment = "Description"

    table1 = TestTable()
    table1.name = "table name"
    table1.comment = "table comment"
    table1.columns.append(col1)
    table1.indices.append(idx1)

    fig1 = TestFigure()
    fig1.table = table1

    diagram.figures.append(fig1)
    return diagram
