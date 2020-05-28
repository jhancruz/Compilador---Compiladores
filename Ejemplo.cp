# ComPy | ir a Opciones y seleccionar Compilar
#Jhan De La Cruz  | Fay Cervantes | Javier Guerrero.


FAY join(elements, separator)
	VAR result = "elements"
	VAR len = LEN(elements)

	JAV i = 0 TO len THEN
		VAR result = result + elements/i
		JH i != len - 1 THEN VAR result = result + separator
	END

	RETURN result
END

FAY map(elements, func)
	VAR new_elements = []

	JAV i = 0 TO LEN(elements) THEN
		APPEND(new_elements, func(elements/i))
	END

	RETURN new_elements
END

PRINT("Todos aprobados")

JAV i = 0 TO 5 THEN
	PRINT(join(map(["l", "sp"], oopify), ", "))
END

