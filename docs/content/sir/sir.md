## Introduction

The SIR model is an epidemiological model used to present the movement of diseases throughout populations. The premise is that one person (AKA individual) is initially infected, and the infection will spread among a population. Under this model, individuals are assigned to **one** of **three** compartments: `S`,`I`, and `R`.

- `S` represents individuals considered susceptible to the disease.
- `I` represents individuals who are infected with the disease at a given moment in time.
- `R` represents individuals who either recovered or succumbed to the disease.

For educational purposes, we are presenting a **simplified** version of this model using COVID-19 as an example to demonstrate how diseases can spread. In actuality, the intricacies of the real world often require highly complex models which account for population changes (births, deaths, immigration, or emigration) and people who are naturally immune to COVID-19. Therefore, we must hold some assumptions as we cannot analyze all factors available.

Some assumptions we will hold are:

- When an individual enters the `R` state, they become *immune* to COVID-19 (no one dies).
- The total population will be *constant*. We will use the population of the United States as of **01/28/2020**: 329,227,746.

Now, we can begin dissecting our SIR model.

***

## Decoding the Model

Before you even begin to decipher the plot above, let us learn about two essential constants: the `b` value and the `k` value.

### The `k` Value

`k` represents the fraction (proportion) of infected individuals that recover every day. Taking the reciprocal of this value (`1/k`) results in the time an infection takes to run its course. After this time period, the individual enters the `R` compartment of the SIR model.

The k value we used in our model is based on real time COVID-19 data is, therefore, constantly changing. **ADD BLURB ON HOW WE CALCULATED K**

### The `b` Value

`b` represents the average count of people infected by an infected individual per day. In real life, finding `k` is plausible, but finding `b` oftentimes ends up being a tricky endeavor. Simulations can be used to estimate `b` but confounding variables are difficult to account for. `b` might also change based on the location we are analyzing. For example, cities have a significantly higher population density than rural areas, meaning they will often have a higher `b` value. In our model, we selected a `b` value of **0.5**, indicating on average, an infected individual would spread the disease to 0.5 people a day (or 1 person every 2 days) during their infectious period.

### Plotting a Pandemic

Taking a look at our plot, you might immediately notice the steep increase in the number of cases at the beginning of the time period. This is a form of **exponential growth**. If we calculate `b/k`, we obtain the total count of infected people one individual generates over the full infectious period of the disease. 

Since our value for `k` is constantly changing, for the purpose of this example, we will assign `k` a value of **0.2**. Calculating `b/k = 0.5/0.2` results in the value **2.5**. This means that, on average, each infected individual will infect 2.5 other people before they recover. We will call this variable which represents the expected count of infections from one person `V`.

If we begin with 1 infection, by the time the first individual is recovered, there are on average **2.5** new infected individuals out there spreading the disease. When this batch of people recovers, there are an additional **6.25** people on average infecting others. This growth is why we observe an immediate uptick in positive cases. **Social distancing** measures slow down this exponential growth, as the `b` value decreases when interactions with others decrease.

### NEXST
 
The assumption that anyone that is recovered is immune and alive allows us to see the impact of the number of people who are recovered increasing. For the beginning of the hypothetical model, the vast majority of people that infected people meet are people who have not yet been exposed. This begins to change once most people have recovered. The odds of exposing a person who has not recovered from the disease gets lower and lower since there are less people who are in the S phase as time progresses. The fraction of infectable people in the population gets lower and lower. We can call this fraction F as a placeholder. We can calculate the effective amount of people getting infected at any point of time by multiplying V and F. We can call this new variable W. Once W is equal to one, the disease stops growing and this is where we see the peak in the number of infected people. From then on W only goes down as we see the infections peter out. In our graph by the time we see a flatline in the amount of infected people, 80% of the people in the population who have been exposed are now recovered. 

The problem with this model is that real life is messy and the population of a group is always variable with new people being born and people dying as a result of the disease or other causes. The model we present to you can only give you a simple idea of the way diseases spread, but in reality the disease would not flatline like we see in the graph due to these variations. One more thing that this model can show you is the concept of herd immunity. The lower the value of F goes over time, the harder it is for the disease to spread. Once the majority of the population is immune the disease has almost completely vanished. This highlights the importance of vaccinations in society. By getting vaccinated we can make the world safer for those who can’t get vaccinated due to health complications. We hope that looking at this model and reading this page has helped you understand a little more about how diseases such as COVID-19 spread on a basic level. If you want to learn more about how this model works you can look at any of the following resources. 

