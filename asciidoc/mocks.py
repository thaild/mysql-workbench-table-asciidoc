# These clssses are for mockking the input data


class TestDiagram:
    figures = []


class TestFigure:
    table = None


class TestTable:
    columns = []
    indices = []
    foreignKeys = []
    name = ""
    comment = ""


class TestColumn:

    class TestSimpleType:
        name = None

    name = None
    autoIncrement = None
    isNotNull = None
    defaultValue = None
    simpleType = TestSimpleType()
    length = None
    defaultValue = None
    comment = None


class TestIndex:
    name = None
    columns = []
    indexType = None
    comment = None


class TestIndexColumn:
    class TestReferencedColumn:
        name = None

    referencedColumn = TestReferencedColumn()


class TestForeignKey:
    columns = []
    referencedColumns = []


class TestForeignKeyColumn:
    name = None


class TestForeignKeyReferenceColumn:
    class TestOwner:
        name = None

    name = None
    owner = TestOwner()
