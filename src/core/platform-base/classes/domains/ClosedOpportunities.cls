public inherited sharing class ClosedOpportunities extends Opportunities{
	public ClosedOpportunities(List<Opportunity> opportunities) {
		this.opportunities = new List<Opportunity>();
		for (Opportunity opportunity : opportunities) {
			if (opportunity.StageName == 'Closed Won') {
				this.opportunities.add(opportunity);
			}
		}
	}
}