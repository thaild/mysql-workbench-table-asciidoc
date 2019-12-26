from asciidoc.generate import generate_asciidoc_schema_documentation


class TestGenerator():
    """Test class for generator
    """
    def test_normal(self, normal_data):
        """Normal case
        """
        asciidoc = generate_asciidoc_schema_documentation(normal_data)
        assert asciidoc is not None
