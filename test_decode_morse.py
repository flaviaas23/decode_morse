import unittest
# from code.desafio.decode_morse import morse_code_to_text
from decode_morse import morse_code_to_text

class TestMorseCodeToText(unittest.TestCase):
    
    def test_single_word(self):
        """
        Teste decodificacao de uma unica palavra.
        """
        self.assertEqual(morse_code_to_text(".... . .-.. .-.. ---"), "HELLO")

    def test_multiple_words(self):
        """
        Teste decodificacao de multiplas palavras. 
        """
        self.assertEqual(morse_code_to_text(".... . -.--   .--- ..- -.. ."), "HEY JUDE")

    def test_numbers(self):
        """
        Teste decodificacao de numeros.
        """
        self.assertEqual(morse_code_to_text(".---- ..--- ...--"), "123")

    def test_letters_and_numbers(self):
        """
        Teste decodificacao de letras e numeros juntos.
        """
        self.assertEqual(morse_code_to_text(".- -... -.-.   .---- ..--- ...--"), "ABC 123")

    def test_invalid_morse_code(self):
        """
        Teste decodificacao de codigo morse invalido.
        """
        self.assertEqual(morse_code_to_text("...---..."), "")  # SOS não está no dicionário

    def test_extra_spaces(self):
        """
        Teste decodificacao com espacos extras.
        """
        self.assertEqual(morse_code_to_text("   .... . -.--   .--- ..- -.. .   "), "HEY JUDE")

if __name__ == '__main__':
    unittest.main()