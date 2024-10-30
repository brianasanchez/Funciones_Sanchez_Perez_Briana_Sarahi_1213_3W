# Funciones_Sanchez_Perez_Briana_Sarahi_1213_3W
Prueba de envio de codigo y screenshot

#Practicando funciones
1- En Python una funcion es definida usando la palabra def como palabra clave 

![image](https://github.com/user-attachments/assets/a90eed4d-519b-47cb-9e42-687e944af0ff)

![image](https://github.com/user-attachments/assets/dfb1a5d8-7cb5-4d5f-9b7c-5a05f9153f5d)

2- Para llamar a una funcion, use la funcion nombrada y seguida de parentesis:

![image](https://github.com/user-attachments/assets/656432c3-1670-46ea-86c9-f863ab2b7020)

![image](https://github.com/user-attachments/assets/1c74e519-ea34-495e-bc74-7f7ac67b9ad9)

3- El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la
función, pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo:

![image](https://github.com/user-attachments/assets/24ec50e0-de19-40d2-8ccc-e0f174547db7)

![image](https://github.com/user-attachments/assets/4cb4860e-b3f0-4868-b93f-b895d46ec0f1)

4- De forma predeterminada, se debe llamar a una función con la cantidad correcta de
argumentos. Lo que significa que si su función espera 2 argumentos, debe llamar a la 
función con 2 argumentos, ni más ni menos.

![image](https://github.com/user-attachments/assets/cef4d766-c08d-4995-9026-d5fa36c55c04)

![image](https://github.com/user-attachments/assets/11ff43da-838b-4c80-9683-53da238b7d7b)

5- Esta función espera 2 argumentos, pero solo obtiene 1:

![image](https://github.com/user-attachments/assets/8226a3bc-0c23-4a71-864a-aa495c75a974)

![image](https://github.com/user-attachments/assets/5bf26b85-e12b-43af-b601-a4c6a2fae02c)

6- Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre 
del parámetro en la definición de la función.
De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los 
elementos en consecuencia:
Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:

![image](https://github.com/user-attachments/assets/0e5d048e-c0fa-42e1-8c76-046f63acafb5)

![image](https://github.com/user-attachments/assets/dc6ab5d0-bfc3-470b-980d-7168d09b020e)

7- También puede enviar argumentos con la sintaxis clave = valor.

De esta forma no importa el orden de los argumentos.

![image](https://github.com/user-attachments/assets/e9e3b582-87ab-435c-bdb3-2d695273c921)

![image](https://github.com/user-attachments/assets/f365a517-2897-4fbd-89fd-48a08edcf6bb)

8- Argumentos arbitrarios de palabras clave, **kwargs
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos
asteriscos: ** antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los
elementos en consecuencia:
Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes
del nombre del parámetro:

![image](https://github.com/user-attachments/assets/585bae87-78c4-4e3e-9511-cba262c51d18)

![image](https://github.com/user-attachments/assets/175fd8cd-6522-4bee-a5bb-762ea3fda41b)

9- Valor de parámetro predeterminado
El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.

![image](https://github.com/user-attachments/assets/2ef64781-18a2-486d-a276-76499a1bdff0)

![image](https://github.com/user-attachments/assets/90bd75df-28d8-41f2-8566-d1b95df83106)

10- Pasar una lista como argumento
Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista,
diccionario, etc.) y será tratado como el mismo tipo de datos dentro de la función.

![image](https://github.com/user-attachments/assets/8b636e9c-e3a8-48d8-b6c3-1afc11643173)

![image](https://github.com/user-attachments/assets/c4d62bc2-0ca8-45d9-9617-176710f00dfa)

11- Regresa Valores
Para permitir que una función devuelva un valor, utilice la declaración de retorno:

![image](https://github.com/user-attachments/assets/07bb6560-16b8-432b-8f07-b7f3e107d328)

![image](https://github.com/user-attachments/assets/5ae91be4-432a-44cd-8ae7-599dd31196d0)

12- La declaración del pass
Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una 
definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.

![image](https://github.com/user-attachments/assets/3f92fc92-1d07-44bf-88d7-369e070e726a)

![image](https://github.com/user-attachments/assets/92df3d19-9739-4cc0-9339-47659774c15f)

13- Argumentos sólo posicionales 
Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO
argumentos de palabras clave.

Para especificar que una función solo puede tener argumentos posicionales, agregue 
, / después de los argumentos:

![image](https://github.com/user-attachments/assets/85316de7-c24e-45a8-a826-e183977ffedb)

![image](https://github.com/user-attachments/assets/85911698-3f39-44d1-95b6-f0bd30b63396)

14
Sin , / en realidad se le permite usar argumentos de palabras clave incluso si la función espera
argumentos posicionales:

![image](https://github.com/user-attachments/assets/1be44a78-e3fb-4571-9520-89437d4bcd97)

![image](https://github.com/user-attachments/assets/7b78db67-dacd-41c9-b183-b78a0cc13627)

15
Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:

![image](https://github.com/user-attachments/assets/6cf04d59-e376-477f-8f82-5ba29ee43e5d)

![image](https://github.com/user-attachments/assets/248da684-a762-47a0-96a0-196dc708ee61)

16
Argumentos de solo palabras clave
Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, 
antes de los argumentos:

![image](https://github.com/user-attachments/assets/0d3bd3e0-cb59-40d0-8fed-56e05e539d93)

![image](https://github.com/user-attachments/assets/6a0b4068-1926-47b0-a078-ef43c173016a)

17
Sin el *, se le permite utilizar argumentos posicionales incluso si la función espera
argumentos de palabras clave:

![image](https://github.com/user-attachments/assets/b854feff-709e-4b6b-a3d8-0f6d03729392)

![image](https://github.com/user-attachments/assets/00db1dfb-b007-4161-97b6-46eb936b740e)

18
Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:

![image](https://github.com/user-attachments/assets/45878077-7762-453d-aee5-e913b8cc2435)

![image](https://github.com/user-attachments/assets/1fc982d6-3f4a-411b-bccb-1aa9d3e54988)

19
Combine solo posicional y solo palabras clave
Puede combinar los dos tipos de argumentos en la misma función.

![image](https://github.com/user-attachments/assets/44f4b016-8377-4901-b8de-6514dac4a32a)

![image](https://github.com/user-attachments/assets/8c6f4cc9-d98c-4b61-b1f9-9a084fc23d1e)

20
Recursividad
Python también acepta la recursividad de funciones, lo que significa que una función
definida puede llamarse a sí misma.

![image](https://github.com/user-attachments/assets/d4fb4db4-4808-4540-a90c-867bb1c9001e)

![image](https://github.com/user-attachments/assets/9087c198-d9bd-486c-8810-0288cb1b39ce)

![image](https://github.com/user-attachments/assets/80b50d0d-1da3-4f4d-9f5d-c2a2647b8f74)











