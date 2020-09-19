## Introduction

The SIR model is an epidemiological model used to present the movement of diseases throughout populations. The premise is that one person (AKA individual) is initially infected, and the infection will spread among a population. Under this model, individuals are assigned to **one** of **three** compartments: `S`,`I`, and `R`.

- `S` represents individuals considered susceptible to the disease.
- `I` represents individuals who are infected with the disease at a given moment in time.
- `R` represents individuals who either recovered or succumbed to the disease.

For educational purposes, we are presenting a **simplified** version of this model using COVID-19 as an example to demonstrate how diseases can spread. In actuality, the intricacies of the real world often require highly complex models which account for population changes (births, deaths, immigration, or emigration) and people who are naturally immune to the disease. Therefore, we must hold some assumptions as we cannot analyze all factors available.

Some assumptions we will hold are:

- When an individual enters the `R` compartment, they become *immune* to the disease (no one dies).
- The total population will be *constant*. We will use the population of the United States as of **01/28/2020**: 329,227,746.

Now, we can begin dissecting our SIR model.

***

## Decoding the Model

Before you even begin to decipher the plot above, let us learn about two essential constants: the `b` value and the `k` value.

### The `k` Value

`k` represents the fraction (proportion) of infected individuals that recover every day. Taking the reciprocal of this value (`1/k`) results in the time an infection takes to run its course. After this time period, the individual enters the `R` compartment of the SIR model.

The `k` value we used in our model is based on real time COVID-19 data is, therefore, constantly changing. A singular `k` value is calculated by dividing the number of recovered people on any given day by the number of positive cases on the previous day. Using this methodology, we calculated `k` values for all of the dates available in the data, then averaged all of them to find the `k` value for the current day.

### The `b` Value

`b` represents the average count of people infected by an infected individual per day. In real life, finding `k` is plausible, but finding `b` oftentimes ends up being a tricky endeavor. Simulations can be used to estimate `b` but confounding variables are difficult to account for. `b` might also change based on the location we are analyzing. For example, cities have a significantly higher population density than rural areas, meaning they will often have a higher `b` value. In our model, we selected a `b` value of **0.5**, indicating on average, an infected individual would spread the disease to 0.5 people a day (or 1 person every 2 days) during their infectious period.

### Plotting a Pandemic

Taking a look at our plot, you might immediately notice the steep increase in the number of cases at the beginning of the time period. This is a form of **exponential growth**. If we calculate `b/k`, we obtain the total count of infected people one individual generates over the full infectious period of the disease. 

Since our value for `k` is constantly changing, for the purpose of this example, we will assign `k` a value of **0.2**. Calculating `b/k = 0.5/0.2` results in the value **2.5**. This means that, on average, each infected individual will infect 2.5 other people before they recover. We will call this variable which represents the expected count of infections from one person `V`.

If we begin with 1 infection, by the time the first individual is recovered, there are on average **2.5** new infected individuals out there spreading the disease. When this batch of people recovers, there are an additional **6.25** people on average infecting others. This growth is why we observe an immediate uptick in positive cases. **Social distancing** measures slow down this exponential growth, as the `b` value decreases when interactions with others decrease.

### Movement of Disease

By assuming that anyone entering the `R` compartment is *immune* to the disease and *alive* enables us to observe how an increasing amount of recovered individuals impacts the spread of disease. At the beginning of this model, the vast majority of people that infected individuals meet are people who have not yet been exposed. However, this begins to change once most individuals have recovered. When individuals recover, they enter the `R` compartment and **leave** the `S` compartment. The odds of exposing a person who has not recovered from the disease decreases greatly because there are **fewer** people who are in the `S` compartment as time progresses. The proportion of susceptible individuals in the population **decreases**.

Let us call this proportion `F` as a placeholder. We can calculate the effective amount of people being infected at any point of time by multiplying `V` and `F`. Let this value be represented by the variable `W`. When `W` is equal to **1**, the rate of infection stops growing, and here we can also observe a peak in the count of infected individuals. Afterwards, `W` only decreases, and the rate of infection peters out. In our model, when the count of infected individuals stabilizes, we can noticed that **80%** of exposed population are now *recovered*. 

***

## Conclusion

The primary drawback of the SIR model is that real life is significantly more complex and contains factors that it cannot account for. A population is always variable: new people are being born and people are dying as a result of the disease or other causes. The model we have presented today is a heavily simplified representation of how diseases spread. We would not observe a flat-line due to these confounding variables.

This model also demonstrates the concept of **herd immunity**. As `F` decreases over time, it is difficult for a disease to spread among a population. Once the majority of a population is immune, the disease has almost completely vanished. This highlights the importance of vaccinations. By being vaccinated, we can make the world safer for those who are unable to be vaccinated due to health complications.

We hope this page has helped you understand at least a little more about how diseases such as COVID-19 spread on a basic level. If you want to learn more about how this model works, take a look at the following resources.

- [Epidemic, Endemic, and Eradication Simulations](https://www.youtube.com/watch?v=7OLpKqTriio)