# Importamos librerías

import streamlit as st 
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px

# Configuración de página :

st.set_page_config(page_title= "Análisis Supervivencia Titanic", layout= "centered" )

# Leemos csv:

titanic=pd.read_csv(r"C:\Users\elena\OneDrive\Escritorio\Samplerepo\MÓDULO 1\13-Trabajo del Módulo I\datos\titanic.csv")

# APP :

st.image ("https://resizer.iproimg.com/unsafe/880x/filters:format(webp)/https://assets.iprofesional.com/assets/jpg/2019/12/488670.jpg", width= 650, caption='Imagen :https://www.iprofesional.com/actualidad/337074-titanic-5-mitos-que-persisten-a-mas-de-un-siglo-del-hundimiento')
st.title("Análisis de la supervivencia en el naufragio del Titanic")
st.text ("Analizamos la supervivencia por edad, sexo, clase, tarifa y embarque")

col1, col2= st.columns(2)

with col1:
    st.write ("¿Cómo afectaron estas variables a la supervivencia?")

with col2:
    st.write('')



# SIDEBAR :

st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.title("Datos sobre supervivencia")
st.sidebar.image("http://c.files.bbci.co.uk/48F4/production/_107767681_5-1.jpg", width=200, caption='Imagen:https://www.bbc.com/mundo/noticias-49429975')
st.sidebar.write("---") # hará un salto de línea 


if st.sidebar.button("Data"):
    
  
   tabs=st.tabs(["Contenido del estudio","Datos importantes","Distribución general de los datos", "Conclusiones"])

   tab_plots= tabs[0]
   with tab_plots:
     st.write("El titanic fue un transatlántico británico que hasta la fecha era el mayor barco de pasajeros del mundo; naufragó en 1912 mientras realizaba su viaje inaugural desde Southampton a Nueva York, tras chocar con un iceberg. En el hundimiento murieron 1496 personas de las 2208 que iban a bordo, entre pasajeros y tripulación; en este estudio basaremos el análisis únicamente en los pasajeros.")
     st.dataframe(titanic) 

   tab_plots= tabs[1]
   with tab_plots:
     st.write("Aunque el trasatlántico tenía capacidad para 3511 pasajeros, solo tenía botes salvavidas para 1178 personas. Además, para agravar la situación, no todos los botes salvavidas cubrieron todas sus plazas durante la evacuación. La mayoría de las casi 1500 víctimas del Titanic fallecieron de hipotermia. También habrían muerto cientos de personas dentro del barco mientras se hundía, la mayoría de ellas familias de inmigrantes que viajaban en tercera clase y que ansiaban comenzar una nueva vida en Estados Unidos.")
     st.dataframe(titanic)

     tab_plots= tabs[2]
     with tab_plots:
        st.write(" En estos gráficos podemos ver un resumen de todo lo analizado, la cantidad de supervivientes, los pasajeros por clases, la districución de las edades , los pasajeros que viajaban con familiares a bordo, y el precio de los tickets que pagaron cada uno.")
        titanic.hist(figsize=(6,7) , color='lightcoral', edgecolor='k' , linewidth= 0.5) 
        st.pyplot()

   tab_plots= tabs[3]
   with tab_plots:
     st.write("Tras haber analizado la supervivencia por edades, clases, por el precio de la tarifa y por el puerto donde embarcaron los pasajeros, podemos concluir que:")
     st.write("1. La supervivencia estaba directamente relacionada con la clase en la que viajaban, teniendo un mayor índice de supervivencia los pasajeros que viajaban en 1ª clase, y altamente relacionada con el precio de la tarifa que pagaron, cuanto mayor fue el importe, mayor fue la probabilidad de supervivencia.")
     st.write("2. La supervivencia fue mayor en mujeres y niños, la mayor parte de los fallecidos fueron hombres.")
     st.write("3. La supervivencia fue mayor en los pasajeros que embarcaron en el puerto de Cherburgo (Francia), por el mayor porcentaje de pasajeros que viajaban en 1ª clase, habiendo un alto porcentaje de fallecidos entre los pasajeros que embarcaron en el puerto británico de salida en Southampton.")
     st.write("A continucación la lista de los pasajeros que sobrevivieron:")
     df=titanic[(titanic['Survived']==1)] 
     st.dataframe(df)


if st.sidebar.button("Análisis por edades"):
    tabs=st.tabs(["Edades de los pasajeros","Pasaje por edades","Relación entre edad y supervivencia"])
    tab_plots= tabs[0]
    with tab_plots:
     st.write("La media de edad era de 29 años, el pasajero de menor edad era un bebe de 4 meses y el mayor tenía 80 años. Viajaban 7 bebes en el barco, todos ellos sobrevivieron, así como la persona de mayor edad, siendo este el único superviviente del rango de edad de mayores de 65 años. Viajaban 44 niños menores de 5 años, de los cuales sobrevivieron 31. De los 590 adultos que viajaban en el barco sobrevivieron 228, siendo este rango de edad el de mayor mortalidad.")
     st.write("Este gráfico nos muestra que la mayoría de los pasajeros tenían edades comprendidas entre los 18 y los 35 años, siendo mayoría los pasajeros en torno a los 25 años, con pocas personas mayores de 65 , muy pocas mayores de 70, y 40 pasajeros menores de 5 años.")
     sns.histplot(x="Age", data=titanic,kde=True,color='darkblue')
     st.pyplot()

    tab_plots=tabs[1]
    with tab_plots:
      st.write("Este gráfico nos muestra los porcentajes por rangos de edades: menores, adultos, mayores de 65 años y edad desconocida que viajaban en el barco:")
      df = pd.DataFrame()
      df['pasajeros']=[113,590,11,177]  
      df['rangos']=[ "Menores de edad", " Adultos"," Mayores 65" , "Edad desconocida"]
      grafico_edades=df
      grafico=px.pie(grafico_edades, values='pasajeros', names='rangos', title='Pasaje por edades' )
      st.plotly_chart(grafico)

    tab_plots= tabs[2]
    with tab_plots:
      st.write("En este gráfico podemos observar como la supervivencia fue más elevada para los menores de 15 años y para los mayores de 55; el gráfico muestra de forma contundente como entre los 18 y los 50 años la supervivencia se redujo drásticamente, por la prioridad que tenían los niños y los ancianos en subir a los botes salvavidas.")
      sns.lineplot(x="Age",y="Survived", data=titanic, color='darkred')
      st.pyplot()




if st.sidebar.button("Análisis supervivencia"):
       tabs=st.tabs(["Supervivientes","Supervivientes por sexos"])
       tab_plots= tabs[0]
       with tab_plots:
        st.write("Analizamos el porcentaje de supervivencia : sobrevivieron 342 pasajeros, el 38 % del pasaje.")
        sns.countplot(x='Survived',data=titanic, palette='dark',hue='Survived')
        st.pyplot()
       tab_plots=tabs[1]
       with tab_plots:
         st.write(" Más del 60 % del pasaje eran hombres, sin embargo podemos comprobar que la mayoría de personas que sobrevivieron eran mujeres, por la prioridad que tuvieron al subir al bote salvavidas, además solo fallecieron 3 mujeres de 1ª clase, siendo el resto de 2 y 3ª clase. En relación a los hombres, los que sobrevivieron en su mayor porcentaje viajaban en 1ª clase.")
         sns.barplot(x='Sex',y='Survived',data=titanic, palette='coolwarm')
         st.pyplot()



if st.sidebar.button("Análisis por clases"):
       tabs=st.tabs(["Pasajeros por clases","Probabilidad supervivencia por clase","Supervivencia por clases"])
       tab_plots= tabs[0]
       with tab_plots:
         st.write("Calculamos el porcentaje de pasajeros por clases: el 55 % del pasaje viajaba en 3ª clase.")
         sns.countplot(x='Pclass',data=titanic, palette='deep')
         st.pyplot()
       tab_plots= tabs[1]
       with tab_plots:
         st.write("Analizamos la probabilidad de supervivencia respecto a la clase: podemos ver como era más probable sobrevivir si viajabas en 1ª clase.")
         sns.lineplot(x ="Pclass", y = "Survived", data=titanic, color = "darkred")
         st.pyplot()
         tab_plots= tabs[2]
         with tab_plots:
          st.write("Mostramos la cantidad de supervivientes en cada clase: el porcentaje de supervivencia de la 1ª clase es del 62 %, frente solo al 24 % de la 3ª clase. Vemos en rojo las personas que fallecieron, pudiendo ver de forma clara el gran porcentaje de personas que fallecieron en 3ª clase.")
          sns.histplot(titanic, x='Pclass', hue= 'Survived', palette='Set1', multiple='stack') 
          st.pyplot()



if st.sidebar.button("Análisis por tarifa"):
      tabs=st.tabs(["Tarifa más alta ","Tarifa más baja","Relación con supervivencia"])
      tab_plots= tabs[0]
      with tab_plots:
         st.write("Comprobamos los pasajeros que pagaron la tarifa más alta: 512 libras, ( teniendo en cuenta que la tarifa media eran 32 libras) ;podemos ver como todos ellos sobrevivieron:")
         df=titanic[titanic['Fare']>=512]
         st.dataframe(df)

      tab_plots= tabs[1]
      with tab_plots:
         st.write("Comprobamos los tickets de la menor tarifa pagada, 0, vemos que varios pasajeros no pagaron o se desconoce el precio de su tarifa, y que sólo uno de este grupo sobrevivió.")
         df=titanic[(titanic['Fare']==0)] 
         st.dataframe(df)

      tab_plots= tabs[2]
      with tab_plots:
          st.write("¿ Qué relación había entre la tarifa mayor y la supervivencia? ")
          st.write("Analizamos la supervivencia de los pasajeros que pagaron más de 100 libras ¿qué porcentaje de supervivencia tuvieron? Podemos comprobar que tenían un porcentaje de supervivencia de",round(titanic[(titanic['Fare']>100) & (titanic['Survived']==1)]['PassengerId'].count() * 100/ titanic[(titanic['Fare']>=100)]['PassengerId'].count(),2),"%")
          
         


if st.sidebar.button("Análisis por puerto de embarque"): 

      tabs=st.tabs(["Tarifas por puerto de embarque ","Pasajeros por puerto de embarque","Probabilidad sobrevivir por puerto de embarque"])
      tab_plots= tabs[0]
      with tab_plots:
         st.write(" Veamos una relación entre la tarifa que pagaron con los puertos donde embarcaron: podemos comprobar que las tarifas más elevadas se pagaron en Cherburgo, donde embarcaron muchos pasajeros de 1ª clase, y las más bajas se abonaron en Queenstown.")
         grafico=px.area(titanic, x='Embarked', y='Fare',title='Tarifas por puerto de embarque', template='plotly_white')
         st.plotly_chart(grafico)

      tab_plots= tabs[1]
      with tab_plots:
         st.write("Podemos comprobar que el 72 % del pasaje embarcó en el puerto inglés de Southampton donde partió el barco, el 18 % embarcó en el puerto francés de Cherburgo, y en su última parada en el puerto irlandés de Queenstown embarcaron un 8 % de pasajeros.")
         grafico_puertos=titanic["Embarked"].value_counts()
         grafico=px.pie(grafico_puertos,values='Embarked', names=['Southampton','Cherburgo','Queenstown'],title='Pasajeros por puerto')
         st.plotly_chart(grafico)

      tab_plots= tabs[2]
      with tab_plots:
         st.write("Vemos la relación de supervivencia por puerto de embarque : podemos comprobar que el mayor porcentaje de supervivencia fue la de los pasajeros embarcados en Cherburgo, donde embarcó gran parte de pasajeros de 1ª clase.")
         st.write(" De las 168 personas que subieron en Cherburgo sobrevivieron 93, un 55 % , ya que como hemos visto antes, muchos de ellos viajaban en 1ªclase.")
         st.write(" De las 644 personas que subieron en Southampton sólo sobrevivieron 217, un 33 % , por lo que la mayor parte de fallecidos provenían de este lugar.")
         st.write(" De las 77 personas que subieron en Queenstown sobrevivieron 30 , un 38 % .")
         grafico=px.area(titanic, x='Embarked', y='Survived',title='Probabilidad de sobrevivir por puerto de embarque', template='plotly_white')
         st.plotly_chart(grafico)
       


if st.sidebar.button("Análisis por familias"): 

    tabs=st.tabs(["Hermanos/as o esposos/as a bordo","Padres/hijos a bordo","Familiares a bordo"])
    tab_plots= tabs[0]
    with tab_plots:
      st.write("Podemos ver que la mayoría del pasaje no viajaba con hermanos/as o esposos/as , muchos de ellos si iban acompañados de un familiar, en menor proporción de dos,de tres, de cuatro, de cinco , y por último , como dato llamativo, una persona de 29 años viajaba con 8 familiares entre esposo/a y hermanos/as.")
      st.image("newplot2.png")

    tab_plots= tabs[1]
    with tab_plots:
      st.write("Podemos ver como muchos de ellos viajaban con padres o hijos, viendo mayor proporción en los niños al ir estos acompañados de sus padres, y algunos adultos con 4 ,5 y 6, llevando con ellos probablemente a sus padres y a todos sus hijos.")
      st.image("newplot.png")

    tab_plots= tabs[2]
    with tab_plots:
      st.write("Comprobamos el porcentaje de supervivencia por familias que viajaban juntas: donde podemos comprobar la mayor supervivencia de las personas que viajaban solas o en compañía de solo un familiar, frente a quien viajaba con muchos familiares, también podemos ver como el índice de supervivencia era menor cuantos familiares acompañaban al pasajero, como dato curioso, podemos ver un pasajero que iba acompañado de 8 familiares , y que no sobrevivió")
      grafico=px.violin(titanic, x='Survived', y=['Parch', 'SibSp'],title=' Supervivencia por familias',template='plotly_white')
      st.plotly_chart(grafico)
     
    







   
   



