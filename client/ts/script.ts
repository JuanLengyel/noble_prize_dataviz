const chartContainer: HTMLElement | null = document.getElementById('main-chart');
const childElement: HTMLElement = document.createElement('p');

childElement.innerHTML = 'This has been added with typescript';

chartContainer?.appendChild(
  childElement
);