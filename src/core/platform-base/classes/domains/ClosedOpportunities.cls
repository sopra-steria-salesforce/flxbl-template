public inherited sharing class ClosedOpportunities extends Opportunities{
	public ClosedOpportunities(List<Opportunity> opportunities) {
		this.opportunities = new List<Opportunity>();
		for (Opportunity opportunity : opportunities) {
			if (opportunity.StageName == 'Closed Won') {
				this.opportunities.add(opportunity);
			}
		}
	}

	public ClosedOpportunities(List<Opportunity> newOpportunities, List<Opportunity> oldOpportunities) {
		this.opportunities = new List<Opportunity>();
		Map<Id, Opportunity> oldOpportunitiesByIds = new Map<Id, Opportunity>(oldOpportunities);
		for (Opportunity newOpportunity : newOpportunities) {
			Opportunity oldOpportunity = oldOpportunitiesByIds.get(newOpportunity.Id);
			if (newOpportunity.StageName == 'Closed Won' && newOpportunity.StageName!=oldOpportunity.StageName) {
				this.opportunities.add(newOpportunity);
			}
		}
	}
}