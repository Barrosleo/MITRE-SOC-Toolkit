// Fetch incident data from the Flask API
fetch('/api/incidents')
  .then(response => response.json())
  .then(data => {
    // For demonstration, tally incidents by a dummy "component" property
    // In a real implementation, incidents would be pre-classified.
    const counts = {
      Adversary: 0,
      Infrastructure: 0,
      Capability: 0,
      Victim: 0,
      Unknown: 0
    };
    data.forEach(incident => {
      // Simple dummy classification based on keywords
      const desc = incident.description.toLowerCase();
      if (desc.includes('apt') || desc.includes('attacker')) {
        counts.Adversary++;
      } else if (desc.includes('server') || desc.includes('domain')) {
        counts.Infrastructure++;
      } else if (desc.includes('exploit') || desc.includes('attack')) {
        counts.Capability++;
      } else if (desc.includes('user') || desc.includes('victim')) {
        counts.Victim++;
      } else {
        counts.Unknown++;
      }
    });
    const labels = Object.keys(counts);
    const values = Object.values(counts);

    const ctx = document.getElementById('attackChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Number of Incidents',
          data: values,
          backgroundColor: [
            'rgba(255, 99, 132, 0.7)',
            'rgba(54, 162, 235, 0.7)',
            'rgba(255, 206, 86, 0.7)',
            'rgba(75, 192, 192, 0.7)',
            'rgba(153, 102, 255, 0.7)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  })
  .catch(error => console.error('Error fetching incidents:', error));
