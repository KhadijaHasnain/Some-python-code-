library(readr)
library(tidyverse)
library(shiny)
library(lubridate)

covid <- read.csv("US_states_covid_data_2023.csv")
covid$date <- ymd(covid$date)


ui <- fluidPage(
  tabsetPanel(
    tabPanel("New Case",
      selectInput(inputId = "state", label="Please select a state", choices=state.name),
      dateInput(inputId = "date", label="Please select a date", min="2020-01-21", max="2023-02-26", value="2020-01-21"),
      textOutput(outputId = "cases")
    ),
    
    tabPanel("Line Graph",
       selectInput(inputId = "state2", label="Please select a state", choices = state.name),
       dateRangeInput(inputId = "date2", label="Please select a date range", min="2020-01-21", max="2023-02-26",
                      start="2020-01-21", end="2023-02-26"),
       actionButton(inputId = "update", label="Submit"),
       plotOutput(outputId = "plot")
    )
    
)
)

server <- function(input,output) {
  output$cases <- renderText(
    {
      covid.1 <- subset(covid, state==input$state)
      covid.1$lag1 <- lag(covid.1$cases)
      covid.1$new.cases <- covid.1$cases - covid.1$lag1
      final <- subset(covid.1, date==input$date)
      paste(input$state, "has", final$new.cases, "new COVID-19 cases on", input$date, ".")
    }
  )
  
  output$plot <- renderPlot(
    {
      state2 <- eventReactive(input$update, input$state2)
      date1 <- eventReactive(input$update, input$date2[1])
      date2 <- eventReactive(input$update, input$date2[2])
      
      covid.2 <- subset(covid, state==state2())
      covid.2$lag1 <- lag(covid.2$cases)
      covid.2$new.cases <- covid.2$cases - covid.2$lag1
      final.2 <- subset(covid.2, date>=date1() & date<=date2())
    
      ggplot(final.2, aes(x=date, y=new.cases)) + 
                  geom_line(color="red", linewidth=0.5) +
                  labs(y="Number of new cases") +
                  theme_classic()
    }
  )
  
}
  

shinyApp(ui = ui, server=server)