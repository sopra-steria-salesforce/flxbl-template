@IsTest
public with sharing class ClosedOpportunitiesTest {

	@IsTest
	static void testOpportunityStageHasNotChangedToAwarded(){
		List<Opportunity> opportunities = new List<Opportunity>{
				new Opportunity(
						Name='Test Opportunity 1',
						StageName='New',
						CloseDate=Date.today().addDays(30)
				),
				new Opportunity(
						Name='Test Opportunity 2',
						StageName='Closed Won',
						CloseDate=Date.today().addDays(30)
				)
		};
		ClosedOpportunities closedOpportunities = new ClosedOpportunities(opportunities);
		Assert.areEqual(1,closedOpportunities.size());
	}
}