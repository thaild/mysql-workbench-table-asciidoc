import grt
import mforms
from wb import *

ModuleInfo = DefineModule(
    name="Schema Document Generator in AsciiDoc",
    author="mhoshino",
    version="1.0",
    description="Generate Asciidoc scehma documentation from a model")


@ModuleInfo.plugin("mhoshino.genSchemaDocAsciiDoc",
                   caption="Generate Schema Documentation in Asciidoc",
                   description="description",
                   input=[wbinputs.currentDiagram()],
                   pluginMenu="Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)
def generate_asciidoc_schema_documentation(diagram):
    """Plugin function to generate schema documentation in AsciiDoc 

    Keyword arguments:
    diagram -- model data
    """
    tableDocs = ''
    tableDocs = ''.join([
        generate_table_doc(x.table) for x in diagram.figures
        if hasattr(x, 'table')
    ])
    docs = '\n'.join([
        '// Generated by Schema Document Generator in AsciiDoc,',
        '// a plugin for MySQL Workbench authored by mhoshino',
        '= Schema documentation',
        ':sectanchors:', 
        ':sectlinks:', 
        ':toc:', 
        tableDocs
        ])

    mforms.Utilities.set_clipboard_text(docs)
    mforms.App.get().set_status_text(
        "The generated documentation is copied to the clipboard. Paste it to use. ")

    print "The generated documentation is copied to the clipboard."

    return 0


def generate_table_doc(table):
    """Generate table layouts in AsciiDoc 

    Keyword arguments:
    table -- table model data
    """

    body = '''
== Table: `{0}`
[.lead]
Description:
--
{1}
--

.Columns
|===
|Column|Datatype|Attributes|Default|Description
{2}

|===

{3}
    '''

    return body.format(
        table.name, 
        table.comment, 
        '\n'.join([generate_column_line(column, table) for column in table.columns]),
        generate_indices_doc(table.indices)
        )


def generate_indices_doc(indices):
    """Generate indices layouts in AsciiDoc 

    Keyword arguments:
    indices -- array of index model data
    """
    if len(indices) <= 0:
        return ''

    body = '''
.Indices
|===
|Name|Columns|Type|Description
{0}
|===
    '''

    return body.format('\n'.join(
        [generate_index_line(index) for index in indices]))


def generate_column_line(column, table):
    """Generate column line in AsciiDoc 

    Keyword arguments:
    column -- column model data
    table -- table model data
    """
    return '|{0}|{1}|{2}|{3}|{4}'.format(
        '{0}'.format(column.name), get_data_type(column),
        generate_attributes(column, table.indices), get_default(column),
        generate_table_description(column, table.foreignKeys))


def generate_table_description(column, fks):
    """Generate the table description

    Keyword arguments:
    column -- column model data
    fks -- foreign keys model data
    """
    description = column.comment

    get_fk_description = lambda x: '\n'.join([
                fk_description, '* Foreign key to {0} on table {1}.'.format(
                    fk.referencedColumns[0].name,
                    fk.referencedColumns[0].owner.name)
            ])

    descriptions = [get_fk_description(fk) for fk in fks if fk.columns[0].name == column.name]
    fk_description = '\n'.join(descriptions)

    if (fk_description != ''):
        description = '\n'.join([description, fk_description])

    return description


def get_default(column):
    """Get the text for default value of the column

    Keyword arguments:
    column -- column model data
    """
    if column.defaultValue is None or column.defaultValue == '':
        return ''

    return '{0}'.format(column.defaultValue)


def generate_attributes(column, indices):
    """Generate texts for the attributes of the column

    Keyword arguments:
    column -- column model data
    indices -- array of index model data
    """
    attributes = []
    for idx in indices:
        for col in idx.columns:
            if col.referencedColumn.name == column.name:
                if idx.indexType == 'PRIMARY':
                    attributes.append('[red]Primary Key')
                    break
                elif idx.indexType == 'UNIQUE':
                    attributes.append('Unique')
                    break
    if column.autoIncrement == 1:
        attributes.append('Auto Increment')
    if column.isNotNull == 1:
        attributes.append('Not NULL')
    return ', '.join(attributes)


def get_data_type(column):
    """Get datatype for the column

    Keyword arguments:
    column -- column model data
    """
    if column.simpleType is None:
        return ''
    return ''.join([column.simpleType.name, get_data_length(column)])


def get_data_length(column):
    """Get data length for the column

    Keyword arguments:
    column -- column model data
    """
    if column.length == -1:
        return ''
    return '({0})'.format(column.length)


def generate_index_line(index):
    """Generate the text line for the index

    Keyword arguments:
    index -- index model data
    """
    return '|{0}|{1}|{2}|{3}'.format(
        index.name, ', '.join([
            '`{0}`'.format(col.referencedColumn.name) for col in index.columns
        ]), index.indexType, index.comment)
